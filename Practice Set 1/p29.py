# Q29. E-Commerce Order System
# User se input lo:
# customer_type
# purchase_amount
# is_member
# Rules:
# 1. Purchase amount <= 0 → "Invalid Amount"
# 2. Agar amount valid hai:
#    - Premium customer:
#      - = ₹10000 → 20% discount
#      - otherwise → 10%
#    - Regular customer:
#      - = ₹10000 → 10%
#      - otherwise → 5%
# 3. Agar customer member hai OR purchase amount >= ₹5000:
#    → "Free Delivery"
# 4. Otherwise:
#    → "Delivery Charges Apply"
# 5. Final amount calculate karo.
# Isme tumhe if, elif, else, nested conditions, and, or aur calculations combine karne hain.
customer_type = input("Enter customer type : ")
purchase_amount = int(input("Enter purchase amount : "))
is_member = input("Are you a member? yes/no : ")

# .lower is liye use kiya hai ki agar "Premium" input ho toh woh "premium" me convert ho jaye
# taki output me dikkat na aye
customer_type = customer_type.lower()
is_member = is_member.lower() 
if purchase_amount <= 0 :
    print("Invalid Amount")
else:
    if customer_type == "premium":
        if purchase_amount >= 10000:
            discount_rate = 20
        else:
            discount_rate = 10
    elif customer_type == "regular":
        if purchase_amount >= 10000:
            discount_rate = 10
        else:
            discount_rate = 5
    else:
        discount_rate = 0
    #discount calculation
    discount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount
    print("Final Amount : ", final_amount)
    #free delivery
    if is_member == "yes" or purchase_amount >= 5000:
        print("Free Delivery")
    else:
        print("Delivery Charges Apply")