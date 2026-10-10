# Q9. Given a list, print all elements that appear more than once in the list.
# [Hint - use set]
number = list(map(int, input("Enter elements : ").split()))
duplicate = set()
for num in number:
    if number.count(num)>1:
        duplicate.add(num)

if duplicate:
    print("Duplicate elements : ",duplicate)
else:
    print("No duplicate elements.")