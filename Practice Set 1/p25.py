# Q25. Employee Eligibility
# Input:
# - Age
# - Experience
# - Qualification
# Employee eligible hai agar:
# Age >= 21
# AND
# Experience >= 2
# AND
# Qualification == "BTech"

# Agar eligible hai:
# - Experience >= 5 → "Senior Candidate"
# - Otherwise → "Eligible Candidate"
# Otherwise "Not Eligible".
age = int(input("Enter age : "))
experience = float(input("Enter experience : "))
qualification = input("Enter qualification : ")
if age >= 21 and experience >= 2 and qualification == "Btech":
    # print("Eligible")
    if experience >= 5 :
        print("Senior Candidate")
    else: 
        print("Eligible Candidate")
else:
    print("Not Elilgible")