class Employ:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class manager(Employ):
    def __init__(self,name,salary,department):
        self.department = department
        Employ.__init__(self,name,salary)
    def display(self):
        print("Name is ",self.name)
        print("Salary is ",self.salary)
        print("Department is ",self.department)
Person = manager("Hamza",13000,"Taxation")
Person.display()