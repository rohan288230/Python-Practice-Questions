# Q15. String mein vowels count karo
text = input("Enter a string : ")
count = 0
for char in text:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
            count += 1

print("Vowels : ",count)