# Q20. Student Admission
# Input:
# - Age
# - Marks
# Rules:
# 1. Pehle check karo age >= 18 hai.
# 2. Agar age eligible hai, tab marks check karo.
# 3. Marks >= 60 → "Admission Eligible"
# 4. Marks < 60 → "Marks Criteria Not Met"
# 5. Age < 18 → "Age Criteria Not Met"
age = int(input("Enter your age : "))
marks = int(input("Enter your marks : "))
if age >= 18:
    if marks >= 60 :
        print("Admission Eligible")
    else:
        print("Marks criteria not met")
else:
    print("Age criteria not met")