# Q2. Write a function that takes two integer a and b and prints 
# all even numbers between them(inclusive).
def even_number(a,b):
    for num in range(a,b+1):
        if num % 2 == 0:
            print(num)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

even_number(num1,num2)