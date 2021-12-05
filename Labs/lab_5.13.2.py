
def split_check(bill, people, tip_percentage=0.15, tax_percentage=0.09):
    return (bill + (bill * tip_percentage) + (bill * tax_percentage)) / people

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))