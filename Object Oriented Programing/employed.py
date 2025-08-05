class employ():
    def __init__(self):
        print("Employ Created ")
    def __del__(self):
        print("Destructor Called ")
def Create_Object():
     obj = employ()
     return(obj)
print("Calling Create_Object()")
obj = Create_Object()
print("Processing.....")


    
    