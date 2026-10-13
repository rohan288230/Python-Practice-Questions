# Q24. Discount Calculator
# Input:
# - Purchase amount
# - Customer type
# Rules:
# Premium:
# - Purchase >= 10000 → 20% discount
# - Otherwise → 10%
# Regular:
# - Purchase >= 10000 → 10%
# - Otherwise → 5%
# Calculate and print:
# - Discount amount
# - Final amount
# Example:
# Purchase = 12000
# Customer = Premium
# Discount = 2400
# Final Amount = 9600
purchase_amount = int(input("Enter Purchase Amount : "))
customer_type = input("Enter Customer Type : ")
customer_type == customer_type.lower()
if customer_type == "premium" :
    if purchase_amount >= 10000:
        discount_rate = 20
    else:
        discount_rate = 10 
elif customer_type == "regular" :
    if purchase_amount >= 10000:
        discount_rate = 10
    else:
        discount_rate = 5
else:
    print("Invalid Customer Type")
    discount_rate = 0
discount = purchase_amount * discount_rate / 100
final_amount = purchase_amount - discount

print("Discount : ", discount)
print("Final Amount : ",final_amount)