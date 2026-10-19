# Q21. List mein maximum number find karo
# Built-in max() use nahi karna.
numbers = [10,20,24,38,49]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum : ",maximum)