# Q8. Let's create a simple Calculator that performs arithmetic operations.
# Create a functtion calculator(a,b,operation) that performs 
# addition, subtraction, multiplication, or division based on the 
# operation parameter.
# [operation parameter can have value '+', '-', '*' & '/']
def calculator(a,b,operation):
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        if b!= 0:
            print(a/b)
        else:
            print("Cannot divide by 0")
    else:
        print("Invalid Operator")

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
op = input("Enter operator (+,-,*,/) : ")

calculator(num1,num2,op)