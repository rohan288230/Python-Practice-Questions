# Q11. User ke number ka factorial nikalo
num = int(input("Enter a number : "))

factorial = 1

for i in range(1,num+1):
    factorial *= i

print("Factorial : ", factorial)