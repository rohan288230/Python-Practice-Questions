# Q10. Ask the user for a string and print:
# - All unique characters
# - The count of unique characters
user = input("Enter a string : ")
count = 0
for ch in user:
    if user.count(ch) == 1:
        print(ch)
        count += 1
print("The count of unique characters : ",count)