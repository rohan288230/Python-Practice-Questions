# Q35. Employee Performance
# Employee sales list:
# sales = [120000, 80000, 150000, 45000, 100000]
# Har employee ko classify karo:
# >= 100000 → Excellent
# >= 75000  → Good
# < 75000   → Needs Improvement
sales = [120000, 80000, 150000, 45000, 100000]
for sale in sales:
    if sale >= 100000:
        print("Excellent")
    elif sale >= 75000:
        print("Good")
    else:
        print("Needs imporvement") 