# Q23. Customer Segmentation
# Input:
# - Total purchase amount
# Classify:
# >= 100000 → Premium Customer
# >= 50000  → Gold Customer
# >= 20000  → Silver Customer
# < 20000   → Regular Customer

# Then additionally check:
# - Premium customer → "Give VIP Benefits"
# - Gold customer → "Give Special Discount"
# Nested condition use karne ki koshish karo.
total_amount = int(input("Enter total purchase amount : "))
if total_amount >= 100000:
    print("Premium Customer")
    print("Give VIP Benefits")
elif total_amount >= 50000:
    print("Gold Customer")
    print("Give Special Discount")
elif total_amount >= 20000:
    print("Silver Customer")
else:
    print("Regular Customer")