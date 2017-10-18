
#library.py

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__',cls,name,bases,body)
        return super().__new__(cls,name,bases,body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()  #the user group has to implement it