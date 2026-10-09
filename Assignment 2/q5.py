# Q5. Write a function to return the sum of digits of a number, n.
def sum_digit(n):
    sum = 0
    while n > 0:
        rem = n % 10 
        sum = sum + rem
        n = n//10
    return sum

num = int(input("Enter a number : "))
print(sum_digit(num))