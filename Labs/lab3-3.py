total_cash = int(input())
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if total_cash == 0:
    print("No change")
else:
    dollars = total_cash // 100
    total_cash = total_cash - (dollars * 100)
    quarters = total_cash // 25
    total_cash = total_cash - (quarters * 25)
    dimes = total_cash // 10
    total_cash = total_cash - (dimes * 10)
    nickels = total_cash // 5
    total_cash = total_cash - (nickels * 5)
    pennies = total_cash

if dollars > 0:
    if dollars == 1:
        print(dollars, "Dollar")
    else:
        print(dollars, "Dollars")
        
if quarters > 0:
    if quarters == 1:
        print(quarters, "Quarter")
    else:
        print(quarters, "Quarters")
        
if dimes > 0:
    if dimes == 1:
        print(dimes, "Dime")
    else:
        print(dimes, "Dimes")
        
if nickels > 0:
    if nickels == 1:
        print(nickels, "Nickel")
    else:
        print(nickels, "Nickels")
        
if pennies > 0:
    if pennies == 1:
        print(pennies, "Penny")
    else:
        print(pennies, "Pennies")
