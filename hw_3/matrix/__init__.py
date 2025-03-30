from copy import deepcopy
from .cache import cache_decorator
import numpy as np


_P = 31  # Показатель и модуль взят маленький чтоб проще было искать колизии
_MOD = 10000


class _Vector(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.n = len(self)

    
    def __matmul__(self, other):
        if self.n != other.n:
            raise ValueError("Different dimensions")
        
        result = 0
        for i in range(self.n):
            result += self[i] * other[i]

        return result

    def __hash__(self):  # В качестве хеш функции будет использован стандартный полиномиальный хеш https://codeforces.com/blog/entry/17507?f0a28=2
        result = 0
        for element in self:
            result = (result * _P + element.__hash__()) % _MOD

        return result


class Matrix():
    def __init__(self, elements):
        self.elements = _Vector([_Vector(row) for row in elements])
        self.n = len(elements)
        if self.n == 0:
            raise ValueError("Matrix must be non empy")

        self.m = len(elements[0])
        if self.m == 0:
            raise ValueError("Matrix must be non empy")
        
        if not all(map(lambda l: len(l) == self.m, self.elements)):
            raise ValueError("All rows must be the same size")
    

    def __getitem__(self, index):
        return self.elements[index]
    

    def __str__(self):
        return "[" + "\n".join([row.__str__() for row in self.elements]) + "]"
    

    def __repr__(self):
        return self.elements.__repr__()
    

    def __neg__(self):
        result = Matrix(deepcopy(self.elements))
        for i, row in enumerate(result.elements):
            result.elements[i] = [-x for x in row]
        
        return result


    def __add__(self, other):
        self._check_same_dimensions(other)
        result = Matrix(deepcopy(self.elements))

        for i, _ in enumerate(result.elements):
            for j, _ in enumerate(result.elements[i]):
                result.elements[i][j] += other.elements[i][j]

        return result


    def __sub__(self, other):
        return self.__add__(-other)


    def __mul__(self, other):
        self._check_same_dimensions(other)

        result = Matrix(deepcopy(self.elements))

        for i, _ in enumerate(result.elements):
            for j, _ in enumerate(result.elements[i]):
                result.elements[i][j] *= other.elements[i][j]

        return result


    @cache_decorator()
    def __matmul__(self, other):
        self._matmul_check_dimensions(other)
        other = other.transperent()

        result = [[] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(other.n):
                result[i].append(self[i] @ other[j])

        return Matrix(result)


    def __eq__(self, other):
        return self.elements == other.elements
    
    def __hash__(self):
        result = 0
        for element in self.elements:
            result = (result * _P + element.__hash__()) % _MOD

        return result


    def transperent(self):
        result = [[] for _ in range(self.m)]
        for row in self.elements:
            for i, element in enumerate(row):
                result[i].append(element)

        return Matrix(result)



    def _check_same_dimensions(self, other):
        if other.n != self.n or self.m != other.m:
            raise ValueError("Different dimensions")

    
    def _matmul_check_dimensions(self, other):
        if self.m != other.n:
            raise ValueError("Wrong dimension, excepted (n, k) @ (k, m)")


def generate_random_matrix():
    gen = np.random.randint(0, 10, (10, 10))
    gen = gen.tolist()
    return Matrix(gen)
