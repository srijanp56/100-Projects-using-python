print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give?\n"))
persons=int(input("How many people to split the bill??\n"))
total_money=(total_bill)+float(tip)
aftersplitng=total_money/int(persons)
print("Each person should pay: rs",round(aftersplitng))