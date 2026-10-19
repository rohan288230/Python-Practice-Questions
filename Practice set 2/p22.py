# Q22. List mein minimum number find karo
number = [10,15,16,13,25,9]

minimum = number[0]

for num in number:
    if num < minimum:
        minimum = num

print("Minimum : ",minimum)