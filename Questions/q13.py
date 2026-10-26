# Q13. Input Validation: User input ko number mein convert karo aur 
# invalid input ke liye error message display karo.
user_input = input("Enter a number : ")
try:
    number = float(user_input)
    print(f"Valid input : {user_input}")
except ValueError:
    print(f"Invalid input : {user_input}")