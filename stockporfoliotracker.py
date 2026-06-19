stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

total_value = 0

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total_value = stocks[stock_name] * quantity
    print("Total Investment Value =", total_value)

    file = open("portfolio.txt", "w")
    file.write("Stock: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Value: " + str(total_value))
    file.close()

    print("Result saved in portfolio.txt")
else:
    print("Stock not found!")