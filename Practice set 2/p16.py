# Q16. String mein spaces count karo
text = input("Enter a string : ")
count = 0

for char in text:
    if char == " ":
        count += 1
print("Spaces : ",count)