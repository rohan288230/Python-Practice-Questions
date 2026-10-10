# Q4. Given a tuple of all even integers, create:
# - A tuple of all even numbers
# - A tuple of all odd numbers
tup = (1,2,3,4,5,6,7,8,9)
even_tup = []
odd_tup = []
for values in tup:
    if values % 2 == 0:
        even_tup.append(values)
    else:
        odd_tup.append(values)
even_tup = tuple(even_tup)
odd_tup = tuple(odd_tup)
print("Even tuple : ",even_tup)
print("Odd tuple : ",odd_tup)