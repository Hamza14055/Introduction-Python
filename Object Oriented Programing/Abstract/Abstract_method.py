from abc import ABC,abstractmethod

class AbsClass(ABC):
    def print (self,x):
        print("Passed value :",x)
    @abstractmethod
    def task(self):
        print("We are in Absclass ")
class test_class(AbsClass):
    def task(self):
        print("We are inside test class ")
test_obj = test_class()
test_obj.task()
test_obj.print(100)