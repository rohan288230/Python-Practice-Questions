# Q10. Student Eligibility
# Age aur marks input lo.
# Student eligible hai agar:
# - Age >= 18 AND
# - Marks >= 60
# Otherwise "Not Eligible".
age = int(input("Enter your age : "))
marks = int(input("Enter your marks : "))
if age >= 18 and marks >= 60:
    print("Eligible")
else:
    print("Not Eligible")