# Q20. List mein even numbers count karo
numbers = [10,15,20,25,30,35,40,45,50]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even number : ",count)