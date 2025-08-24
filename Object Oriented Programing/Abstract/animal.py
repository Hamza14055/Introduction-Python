from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk ")
class Dog(Animal):
    def move(self):
        print("I can bark ")
class Snake(Animal):
    def move(self):
        print("I can slither")
H = Human()
H.move()
D = Dog()
D.move()
S = Snake()
S.move()
