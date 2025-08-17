class Myclass:
    __privatevar = 27
    def __privmeth(self):
        print("The Number is 27")
    def hello(self):
        print("The value is ",Myclass.__privatevar)
obj = Myclass()
obj.hello()
obj.__privmeth()