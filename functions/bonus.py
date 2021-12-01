def findBonus(selling_price, buying_price):
    """This function will calculate the profit
    and prints the  the bonus.
    """
    profit = selling_price-buying_price
    if selling_price > buying_price:
        bonus = 0.05 * profit
        print(f"Congrats!! You have made a bonus of Ksh: {bonus}")
        print(f"Net Profit: {profit}")
        print(f"Selling Price :{selling_price} ")
        print(f"Buying Price :{buying_price} ")

    else:
        print("You have made a loss")


selling_price = int(input("Enter the selling price:\n"))
buying_price = int(input("Enter the buying price:\n"))
print(findBonus(selling_price, buying_price))
