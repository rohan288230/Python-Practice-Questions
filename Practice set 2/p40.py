# Q40. Sales Analysis
# sales = [12000, 45000, 78000, 23000, 91000, 34000, 67000]
# Loop use karke find karo:
# 1. Total sales
# 2. Average sales
# 3. Highest sales
# 4. Lowest sales
# 5. Sales above ₹50,000
# 6. Number of sales transactions
# 7. Number of transactions below ₹30,000
sales = [12000, 45000, 78000, 23000, 91000, 34000, 67000]
# Total sales
total = 0
for sale in sales:
    total += sale
# Average sales
average = total/len(sales)
# Highest sales
highest = sales[0]
for sale in sales:
    if sale > highest:
        highest = sale
# Lowest sales
lowest = sales[0]
for sale in sales:
    if sale < lowest:
        lowest = sale
# Sales above 50000
above_50000 = 0
for sale in sales:
    if sale >= 50000:
        above_50000 += 1
# Number of transactions 
transaction = len(sales)
# Transactions below 30000
below_30000 = 0
for sale in sales:
    if sale < 30000:
        below_30000 += 1

print("Total sales : ",total)
print("Average sales : ",average)
print("Highest sales : ",highest)
print("Lowest sales : ",lowest)
print("Sales above 50000 : ",above_50000)
print("Number of transactions : ",transaction)
print("Transactions below 30000 : ", below_30000)