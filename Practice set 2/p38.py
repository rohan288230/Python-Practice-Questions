# Q38. Second largest number
# numbers = [10, 25, 7, 40, 32, 18]
# max() use nahi karna.
numbers = [10, 25, 7, 40, 32, 18]
largest = float("-inf")
second_largest = float("-inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num!= largest:
        second_largest = num
print("Largest : ", largest)
print("Second largest : ", second_largest)