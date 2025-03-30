import numpy as np

class Complex():
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img


    @property
    def real(self):
        return self._real
    

    @property
    def img(self):
        return self._img
    

    @real.setter
    def real(self, value):
        self._real = value

    
    @img.setter
    def img(self, value):
        self._img = value


    def conjugate(self):
        return Complex(self.real, -self.img)

    
    def __neg__(self):
        return Complex(-self.real, -self.img)

    
    def __iadd__(self, other):
        self.real += other.real
        self.img += other.img
        return self

    
    def __isub__(self, other):
        return self.__iadd__(-other)


    def __imul__(self, other):
        new_real = self.real * other.real - self.img * other.img
        new_img = self.img * other.real + self.real * other.img

        self.real = new_real
        self.img = new_img
        return self


    def __add__(self, other):
        result = Complex(self.real, self.img)
        result += other
        return result

    
    def __sub__(self, other):
        return self.__add__(-other)
    

    def __mul__(self, other):
        result = Complex(self.real, self.img)
        result *= other
        return result
    

    def __itruediv__(self, other):
        numerator = Complex(self.real, self.img)
        denominator = Complex(other.real, other.img)
        
        numerator *= other.conjugate()
        denominator *= other.conjugate()

        self.real = numerator.real / denominator.real
        self.img = numerator.img / denominator.real
        return self


    def __truediv__(self, other):
        result = Complex(self.real, self.img)
        result /= other
        return result
    
    
    def __ipow__(self, deg):
        multiplier = Complex(self.real, self.img)
        for _ in range(deg):
            self *= multiplier
        
        return self
    

    def __pow__(self, deg):
        result = Complex(self.real, self.img)
        result **= deg
        return result
    

    def __str__(self):
        if self.img < 0:
            return f"{self.real} - {-self.img}i";
        else:
            return f"{self.real} + {self.img}i";


    def save(self, filename):
        pass


    def load(self, filename):
        pass
        