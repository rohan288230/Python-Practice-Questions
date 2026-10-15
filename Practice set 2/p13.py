# Q13. Number ke digits ka sum nikalo
# Example:
# Input: 458
# 4 + 5 + 8 = 17
num = int(input("Enter a number : "))

total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Digit sum : ",total)