# Q11. Employee Bonus
# Employee ki salary aur performance rating input lo.
# Bonus milega agar:
# - Salary < 50000 AND
# - Rating >= 8
# Otherwise "No Bonus".
salary = int(input("Enter your salary : "))
rate = int(input("Enter your performance rating : "))
if salary < 50000 and rate >= 8:
    print("Bonus")
else:
    print("No Bonus")