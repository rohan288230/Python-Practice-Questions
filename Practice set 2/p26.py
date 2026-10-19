# Q26. List mein negative numbers skip karo
numbers = [10,-5,20,-8,30,-23]

for num in numbers:
    if num < 0:
        continue
    print(num)