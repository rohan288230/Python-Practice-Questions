# Q17. Profile Validator: Name, age aur email input lekar 
# empty name aur invalid age jaise cases reject karo.
name = input("Enter name : ").strip()
age = (input("Enter age : ")).strip()
email = input("Enter email : ").strip()

if not name:
    print("Invalid : Name cannot be empty.")
elif not age.isdigit():
    print("Invalid : Age must be whole number.")
elif int(age) <= 0 or int(age) > 120:
    print("Invalid : Age must be between 1 and 120.")
elif not email or "@" not in email or "." not in email.split("@")[-1]:
    print("Invalid : Please enter a valid email.")
else:
    age = int(age)
    print("Profile is valid.")
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Email : {email}")