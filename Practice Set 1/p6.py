# Q6. Marks Classification
# Marks input lo:
# - 90–100 → "A"
# - 75–89 → "B"
# - 60–74 → "C"
# - 40–59 → "D"
# - Below 40 → "Fail"
# 100 se zyada ya 0 se kam marks aaye to "Invalid Marks" print karo.
marks = int(input("Enter your marks : "))
if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >=90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")