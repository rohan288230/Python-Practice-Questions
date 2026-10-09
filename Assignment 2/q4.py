# Q4. Write a function to return the count the number of digits in number,n
def number_digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

num = int(input("Enter a number : "))
print(number_digit(num))