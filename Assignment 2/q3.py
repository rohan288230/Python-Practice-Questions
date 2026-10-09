# Q3. Write a function that prints the digit of a number, n.
# For eg: n = 312, there are 3 digits in it 3,1 and 2 & 
# we need to print the.

def digit(n):
    while n > 0:
        print(n%10)
        n = n//10
num = int(input("Enter a number : "))
digit(num)