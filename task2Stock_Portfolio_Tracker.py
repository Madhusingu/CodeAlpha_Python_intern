
# Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 130
}

portfolio = {}  # To store user input
total_value = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Invalid stock. Try again.")
        continue
    qty = input(f"Enter quantity for {stock}: ")
    if not qty.isdigit():
        print("❌ Quantity must be a number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + int(qty)

# Display results
print("\n📦 Portfolio Summary")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")

# Optional: Save to text file
with open("portfolio_summary.txt", "w", encoding="utf-8") as file:

    file.write("Stock Portfolio Summary\n\n")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        file.write(f"{stock}: {qty} × ₹{stock_prices[stock]} = ₹{value}\n")
    file.write(f"\nTotal Value: ₹{total_value}\n")
print("📁 Saved to 'portfolio_summary.txt'")
