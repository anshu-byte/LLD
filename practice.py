# “Object-oriented programming offers a sustainable way to write spaghetti code.” — Paul Graham
# https://medium.com/pythoneers/mastering-the-art-of-object-oriented-programming-in-python-df04c83cc15b


# Inheritance
# It is the capability of one class to derive or inherit the properties from another class
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


# Single Inheritance
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Multiple Inheritance
class Square(Rectangle, Shape):
    def __init__(self, side):
        self.width = side
        self.height = side


# When a class inherits from multiple classes that define a method with the same name,
# python uses a method resolution order (MRO) algorithm to determine which method should be
# called. The C3 algorithm is the most common MRO in python, this algorithm is used to resolve
# the order of method calls in the case of multiple inheritance and ensure that the order
# is predictable and efficient.

# Encapsulation
# It is the practice of hiding the internal implementation details of an object
# from other parts of the program


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def _get_age(self):
        return self.__age

    def get_age(self):
        return self._get_age()


# Polymorphism

# Method overriding occurs when a subclass provides a different implementation of a method
# that is already defined in the parent class.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)


# Method overloading is not supported in python. (two methods cannot have the same name in Python)
# we can achieve the same behavior with methods that take different arguments and have different
# behavior depending on the type of argument. (use none as default value for arguments)


# Abstraction
# Data abstraction is the practice of hiding the implementation details of an object
# from other parts of the program and providing only a simplified public interface to
# interact with the object
from abc import ABC, abstractmethod


class Shape2(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle2(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":

    print("...Inheritance...")
    rectangle = Rectangle(5, 6)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())

    square = Square(4)
    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())

    print()

    print("...Encapsulation...")
    person = Person("Anshu", 23)
    print("Anshu Age:", person.get_age())

    print()

    print("...Polymorphism...")
    circle = Circle(1)
    print("Area of Circle", circle.area())

    print()
    print("...Abstraction...")
    rectangle2 = Rectangle2(5, 6)
    print("Rectangle Area:", rectangle2.area())
    print("Rectangle Perimeter:", rectangle2.perimeter())
