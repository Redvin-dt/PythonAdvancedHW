from matrix import generate_random_matrix
from copy import deepcopy

def find_collisions_matrix():
    a = generate_random_matrix()

    b = generate_random_matrix()
    while a.__hash__() == b.__hash__():
        b = generate_random_matrix()

    c = generate_random_matrix()
    while a.__hash__() != c.__hash__() or a == c:
        c = generate_random_matrix()

    d = deepcopy(b)

    if a @ b == c @ d:
        return find_collisions_matrix()

    return (a, b, c, d)
    