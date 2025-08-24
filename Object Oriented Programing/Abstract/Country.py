class USA():
    def capital(self):
        print("The Capital of USA is Washington D.C ")
    def language(self):
        print("The Language of USA is english ")
    def Type(self):
        print("USA is a developed country")
class India():
    def capital(self):
        print("The Capital of India is Delhi")
    def language(self):
        print("Hindi is the national language of India ")
    def Type(self):
        print("India is a developing country")
I = India()
U = USA()
for countries in(I,U):
    countries.capital()
    countries.language()
    countries.Type()
    
