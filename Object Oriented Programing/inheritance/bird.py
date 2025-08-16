class bird :
    def __init__(self,name,colour):
        self.name = name 
        self.colour = colour
    def display(self):
        print("The name is : ",self.name)
        print("The colour is  : ",self.colour)
    def move():
        print("This bird can't fly ")
class penguin(bird):
    def __init__(self,name,colour):
        super().__init__(name,colour)
        print("Penguins live in Antartica ")
    def display_1(self):
        print("Penguins can't survive in hot areas ")
obj = penguin("Penguin","black")
obj.display()
obj.display_1()

    