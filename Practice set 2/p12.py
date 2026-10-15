# Q12. Number ke digits count karo
# Input: 45872
# Output: 5 digits
num = int(input("Enter a number : "))

count = 0

while num > 0:
    num = num//10
    count += 1

print("Number of digits : ",count)