number = int(input("Enter the number "))


class Roman:
    def program(self, Number,digits):
        digits = []
    while Number != 0:
       digit = Number % 10     
       digits.append(digit)    
        Number = Number // 10  
        digits[::-1] 
        number = int(input("Enter the number: "))
        roman_map = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X"
        }

        if Number in roman_map:
            print(roman_map[Number])
        else:
            print("Number out of range (1–10 supported).")
        

p = Roman()
p.program(Number)

     




       