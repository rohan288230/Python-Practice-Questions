# Q22. Profit/Loss Analysis
# Input:
# - Cost Price
# - Selling Price
# Calculate:
# profit = selling_price - cost_price

# Rules:
# - Profit > 0 → "Profit"
# - Profit < 0 → "Loss"
# - Profit == 0 → "No Profit No Loss"
# Agar profit hai, further classify:
# - Profit >= ₹10,000 → "High Profit"
# - Otherwise → "Low Profit"
cp = int(input("Enter cost price : "))
sp = int(input("Enter selling price : "))
profit = sp - cp
if profit > 0:
    print("Profit")
    if profit >= 10000:
        print("High Profit")
    else:
        print("Low Profit")
elif profit < 0:
    print("Loss")
else:
    print("No Profit No Loss")