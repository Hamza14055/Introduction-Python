class person :
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def show_info(self):
        print("The name is ",self.name,"The age is",self.age)
man_1 = person("Hamza",16)
man_1.show_info()