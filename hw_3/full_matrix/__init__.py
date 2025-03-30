import numpy as np

class FullMatrix():
    def __init__(self, elements):
        self._check_elements(elements)
        self.elements = np.array(elements)


    def __getitem__(self, index):
        return self.elements[index]
    

    @property
    def elements(self):
        return self._elements
    

    @property
    def n(self):
        return self._n
    

    @property
    def m(self):
        return self._m


    @elements.setter
    def elements(self, value):
        self._check_elements(value)
        self._n = len(value)
        self._m = len(value[0])
        self._elements = value


    @staticmethod
    def _check_elements(elements):
        n = len(elements)
        if n == 0:
            raise ValueError("Matrix must be non empy")
        
        m = len(elements[0])
        if m == 0:
            raise ValueError("Matrix must be non empy")
        
        if not all(map(lambda l: len(l) == m, elements)):
            raise ValueError("All rows must be the same size")

    
    def __neg__(self):
        return FullMatrix(-self.elements)
    
    def __iadd__(self, other):
        self.elements += other.elements
        return self

    
    def __isub__(self, other):
        return self.__iadd__(-other)


    def __imul__(self, other):
        self.elements *= other.elements
        return self


    def __add__(self, other):
        result = FullMatrix(self.elements)
        result += other
        return result

    
    def __sub__(self, other):
        return self.__add__(-other)
    

    def __mul__(self, other):
        result = FullMatrix(self.elements)
        result *= other
        return result
    

    def __itruediv__(self, other):
        self.elements = np.divide(self.elements, other.elements)
        return self


    def __truediv__(self, other):
        result = FullMatrix(self.elements)
        result /= other
        return result
    
    
    def __ipow__(self, deg):
        self.elements = np.linalg.matrix_power(self.elements, deg)
        return self
    

    def __pow__(self, deg):
        result = FullMatrix(np.linalg.matrix_power(self.elements, deg))
        return result
    

    def __imatmul__(self, other):
        self.elements = self.elements @ other.elemetns
        return self


    def __matmul__(self, other):
        return self.elements @ other.elements
  

    def __str__(self):
        return np.array_str(self.elements)


    def save(self, filename):
        np.save(filename, self.elements)


    def load(self, filename):
        np.load(filename, self.elements)
        

def generate_full_matrix():
    gen = np.random.randint(1, 10, (10, 10))
    gen = gen.tolist()
    return FullMatrix(gen)