# Q15. Job Eligibility
# Candidate ki degree aur experience input lo.
# Candidate eligible hai agar:
# - Degree "BTech" OR
# - Degree "BCA"
# AND experience >= 1 year.
# Yahan dhyan dena: or aur and dono use honge.
degree = input("Enter your degree : ")
experience = int(input("Enter your experience : "))
if degree == "Btech" or degree == "BCA" and experience >= 1:
    print("Eligible")
else:
    print("Not Eligible")