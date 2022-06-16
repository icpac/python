import abc
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        print("Soy un poligono")
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        super().noofsides()
        print(" I have 3 sides ");


class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        super().noofsides
        print(" I have 5 sides");


# Driver code
R = Triangle();
R.noofsides()


class Parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"

class Child(Parent):
    @property
    def geeks(self):
        return "child class"


try:
    r = Parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = Child()
print(r.geeks)