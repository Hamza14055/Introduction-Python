def TotalBill(bill_amt,tip_perc):
    Tot = bill_amt*(1+(1/100)*tip_perc)
    print(int (Tot))

bill_amt = int(input("Enter the Bill ammount : "))
tip_perc = int(input("Enter the tip percentage : "))
TotalBill(bill_amt,tip_perc)
