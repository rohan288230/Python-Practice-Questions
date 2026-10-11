# Q7. Sales Classification
# Monthly sales input lo:
# - Sales >= 100000 → "Excellent"
# - Sales >= 75000 → "Very Good"
# - Sales >= 50000 → "Good"
# - Sales >= 25000 → "Average"
# - Otherwise → "Poor"
sales = int(input("Enter Monthly Sales : "))
if sales >= 100000:
    print("Excellent")
elif sales >= 75000:
    print("Very Good")
elif sales >= 50000:
    print("Good")
elif sales >= 25000:
    print("Average")
else:
    print("Poor")