# Q8. Simple Bill: Price aur quantity input lekar total bill calculate
# karo aur amount ko 2 decimal places tak display karo.
price = float(input("Enter price : "))
quantity = int(input("Enter quantity : "))
total_bill = price * quantity
print(f"Total Bill : {total_bill:.2f}")