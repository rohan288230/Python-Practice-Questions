# Q14. Free Delivery
# Order amount aur membership input lo.
# Free delivery milegi agar:
# - Order amount >= ₹1000 OR
# - Customer premium member hai.
# Otherwise delivery charge lagega.
amount = int(input("Enter order amount : "))
membership = input("Enter membership status : ")
if amount >= 1000 or membership == "premium" :
    print("Free delivery")
else:
    print("Delivery Charges Apply")