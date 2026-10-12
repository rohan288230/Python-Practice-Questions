# Q16. Exam Permission
# Student ke paas ID card aur admit card hai ya nahi input lo.
# Exam dene ki permission milegi agar:
# - ID card available OR
# - Admit card available
idcard = input("ID Card Present : ")
admitcard = input("Admit Card Present : ")
if idcard == "yes" or admitcard == "yes":
    print("Permission granted for exam.")
else:
    print("No permission.")