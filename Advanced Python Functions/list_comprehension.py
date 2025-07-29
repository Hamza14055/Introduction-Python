num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
print("List of odd numbers:", odd_numbers)

fruits = ['apple', 'banana', 'mango', 'orange']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruit list:", capitalized_fruits)
