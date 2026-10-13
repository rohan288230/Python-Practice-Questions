# Q30. Final Data Analyst Challenge
# Ek company employee ko performance ke basis par classify karna chahti hai.
# Inputs:
# sales
# target
# attendance
# rating

# Rules:
# - Agar attendance < 75 → "Not Eligible for Bonus"
# - Otherwise:
#   - Sales >= Target AND rating >= 8 → "High Performer"
#   - Sales >= Target OR rating >= 8 → "Good Performer"
#   - Otherwise → "Needs Improvement"
# High Performer ke liye:
# - Agar sales >= Target × 1.2 → "20% Bonus"
# - Otherwise → "10% Bonus"
# Is question ko khud structure karo. Main iska solution abhi nahi dunga.
sales = int(input("Enter your sales : "))
target = int(input("Enter your target : "))
attendance = int(input("Enter your attendance : "))
rating = int(input("Enter your rating : "))
if attendance < 75 :
    print("Not Eligible For Bonus")
else:
    if sales >= target and rating >= 8 :
        print("High Performer")
        if sales >= target * 1.2 :
            print("20 % Bonus")
        else:
            print("10 % Bonus")
    elif sales >= target or rating >= 8 :
        print("Good Performer")
    else:
        print("Need Improverment")