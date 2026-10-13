# Q21. Sales Performance
# Input:
# - Sales
# - Target
# Rules:
# - Sales >= Target → "Target Achieved"
# - Sales < Target → "Target Not Achieved"
# Agar target achieve hua hai to further check karo:
# - Sales >= Target × 1.2 → "Excellent Performance"
# - Otherwise → "Good Performance"
sales = int(input("Enter your sales : "))
target = int(input("Enter your target : "))
if sales >= target:
    print("Target Achieved")
    if sales >= target * 1.2 :
        print("Excellent performance")
    else:
        print("Good Performance")
else:
    print("Target not achieved")