# Q9. Electricity Bill Category
# Units consumed input lo:
# - 0–100 → "Low Usage"
# - 101–300 → "Medium Usage"
# - 301–500 → "High Usage"
# - Above 500 → "Very High Usage"
bill = int(input("Enter your Electricity Bill : "))
if bill < 0 :
    print("Invalid Bill")
elif bill <= 100 :
    print("Low Usage")
elif bill <= 300:
    print("Medium Usage")
elif bill <= 500:
    print("High Usage")
else :
    print("Very High Usage")
