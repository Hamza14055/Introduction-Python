class person :
    def __init__(self,name,id_number):
        self.name = name
        self.id = id_number
    def display(self):
        print("Name is ",self.name)
        print("ID number is ",self.id)
class employ(person):
    def __init__(self,name,id_number,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id_number)
    def display_salary(self):
        print("Salary is : ",self.salary)
obj = employ("Hamza",1967,13000,"Manager")
obj.display()
obj.display_salary()
        
