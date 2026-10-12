# Q13. Discount Eligibility
# Customer ka purchase amount aur membership status input lo.
# Discount milega agar:
# - Purchase >= 5000 AND
# - Customer "premium" member ho.
# Otherwise no discount.
purchase = int(input("Enter your purchase amount : "))
membership = input("Enter your membership status : ")
if purchase >= 5000 and membership == "premium":
    print("Discount")
else:
    print("No Discount")