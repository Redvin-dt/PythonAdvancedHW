from functools import wraps
from collections import deque

_DEFAULT_CACHE_SIZE = 100

def cache_decorator(cache_size=_DEFAULT_CACHE_SIZE):
    def decorator(f):
        cache = {}
        order = deque()

        @wraps(f)
        def wrapper(*args, **kwargs):
            use_cache = kwargs.pop('use_cache', True)
            
            if not use_cache:
                return f(*args, **kwargs)

            cached_key = map(lambda arg: arg.__hash__(), args)


            if cached_key in cache:
                order.remove(cached_key)
                order.append(cached_key)
                return cache[cached_key].value

            result = f(*args, **kwargs)
            cache[cached_key] = result

            if len(order) == cache_size:
                expired_key = order.popleft()
                del cache[expired_key]
                order.append(cached_key)
            
            return result
        
        return wrapper
    return decorator
