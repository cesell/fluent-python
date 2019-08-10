from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #choose __repr__, because when no custom __str__ Python will call __repr__
        #return 'Vector(%r,%r)' % (self.x,self.y)
        return 'Vector({},{})'.format(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        '''
        returns False if the maggitude of the vector is zero, True otherwise. 
        '''
        return bool(abs(self))
        #return bool(self.x or self.y)


# Overloading operators

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)
