# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

def split_check(bill, people=1, default_tax_percentage=0.09, default_tip_percentage=0.15):
    total_bill = bill + (bill * default_tax_percentage) + (bill * default_tip_percentage)
    split_it = total_bill / people
    return (split_it)


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