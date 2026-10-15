# Q17. String ko reverse karo using loop
text = input("Enter a string : ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reverse : ",reverse)