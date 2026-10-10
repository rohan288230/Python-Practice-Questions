# Q2. Given a list of integers compute the average of all numbers in the list
list = [10,15,20,25,30]
total = 0
for values in list:
    total += values
average = total / len(list)
print("Average : ",average)