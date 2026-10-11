# Q1. Positive / Negative
# User se ek number lo.
# - Number positive hai → "Positive"
# - Number negative hai → "Negative"
# - Number 0 hai → "Zero"
num = int(input("Enter a number : "))
if num > 0:
    print("Number is positive.")
elif num < 0:
        print("Number is negative.")
else:
    print("Number is 0.")