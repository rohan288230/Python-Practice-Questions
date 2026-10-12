# Q12. Login System
# Username aur password input lo.
# Login successful tabhi ho jab:
# - Username "admin" ho
# - AND password "1234" ho
# Otherwise "Invalid Login".
username = input("Enter username : ")
password = int(input("Enter password : "))
if username == "admin" and password == 1234 :
    print("Login successful")
else:
    print("Invalid Login")