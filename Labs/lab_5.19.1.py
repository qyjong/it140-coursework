
def exact_change(value):
    if value == 0: # if input is zero, it prints "no change" and returns all zeroes
        print("no change")
        return 0, 0, 0, 0, 0
    dollars = value // 100 # divides with no remainders by 100
    value -= dollars * 100 # then subtracts that amount from value
    quarters = value // 25
    value -= quarters * 25
    dimes = value // 10
    value -= dimes * 10
    nickels = value // 5
    value -= nickels * 5
    pennies = value
    return dollars, quarters, dimes, nickels, pennies

if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 0:
        if num_dollars == 1: # checks if dollar(s) is singular or plural
            print(num_dollars, "dollar")
        else:
            print(num_dollars, "dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(num_quarters, "quarter")
        else:
            print(num_quarters, "quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(num_dimes, "dime")
        else:
            print(num_dimes, "dimes")
    
    if num_nickels > 0:
        if num_nickels == 1:
            print(num_nickels, "nickel")
        else:
            print(num_nickels, "nickels")
    
    if num_pennies > 0:
        if num_pennies == 1:
            print(num_pennies, "penny")
        else:
            print(num_pennies, "pennies")
