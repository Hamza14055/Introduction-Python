def hotel_days(days):
    return 200*days
def ride_cost(city):
    if city == "karachi":
        return 140
    elif city == "hyderabad":
        return 130 
    elif city == "gwadar":
        return 250
def vehicle_cost(days):
    if days<= 7 :
        return (110*days)-10
    if days<=20 and days>10:
        return (110*days)-30
    if days>30 :
        return(110*days)-50
def total_cost(city,days,spending_money):
    total = hotel_days(days)+ride_cost(city)+vehicle_cost(days)+spending_money
    return total
    
spending_money = int(input("Enter the money you spent "))
city = input("Enter the city you want to travel to karachi/gwadar/hyderabad")
days = int(input("Enter the ammount of days you will spend"))
print("Cost of trip",total_cost(city,days,spending_money))