class parrot :
    species = "Bird"
    def __init__(self,color,name):
        self.color = color
        self.name = name 
Australian_Parrot = parrot("Yellow","Australian Parrot")
print("The color of this parrot is ",Australian_Parrot.color)
print(Australian_Parrot.name,"is the name of this parrot ")
print("The species is ",Australian_Parrot.species)