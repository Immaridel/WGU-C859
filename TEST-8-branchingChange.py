total = int(input())
if total == 0:
    print("No change")
else:
    money = [(100, "Dollar", "Dollars"),
             (25, "Quarter", "Quarters"),
             (10, "Dime", "Dimes"),
             (5, "Nickel", "Nickels"),
             (1, "Penny", "Pennies")]
    for i in money:
        coins = total // i[0]
        total %= i[0]
        if coins > 1:
            print(f"{coins} {i[2]}")
        elif coins == 1:
            print(f"1 {i[1]}")