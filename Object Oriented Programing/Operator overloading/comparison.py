class A:
    def __init__(self,a):
        self.a = a 
    def __lt__(self,other):
        if(self.a < other.a):
            return("Obj1 is lesser than Obj2")
        else :
            return("Obj2 is lesser than Obj1")
    def __eq__(self,other):
        if(self.a == other.a):
            return("Obj1 is equal to Obj2 ")
        else:
            return("Obj1 is not equal to Obj2")
Obj1 = A(2)
Obj2 = A(3)
print("Passed Values ",Obj1.a,Obj2.a)
print(Obj1<Obj2)

Obj3 = A(4)
Obj4 = A(4)
print("Passed values ",Obj3.a,Obj4.a)
print(Obj3==Obj4)
        
    