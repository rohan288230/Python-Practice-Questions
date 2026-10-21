# Q36. Customer Discount
# purchases = [5000, 12000, 3000, 15000, 8000]
# Rules:
# >= 10000 → 20% discount
# >= 5000  → 10% discount
# < 5000   → No discount
purchases = [5000, 12000, 3000, 15000, 8000]
for amount in purchases:
    if amount >= 10000:
        discount = amount * 20 / 100
    elif amount >= 5000:
        discount = amount * 10 / 100
    else:
        discount = 0
    final_amount = amount - discount
    print("Purchase : ", amount)
    print("Discount : ",discount)
    print("Final Amount : ", final_amount)
    print()