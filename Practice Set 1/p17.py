# Q17. Account Verification
# Input lo:
# is_verified = True/False

# Agar account verified nahi hai, print:
# # "Please verify your account"
# Otherwise:
# "Account Verified"
# Yahan not use karo.
is_verified = input("Is account verified? True/False: ")

is_verified = is_verified.lower() == "true"

if not is_verified:
    print("Please verify your account")
else:
    print("Account Verified")