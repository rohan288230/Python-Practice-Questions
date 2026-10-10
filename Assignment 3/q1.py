# Q1. Ask the user for a string and check whether it is palindrome or not.
# A palindrome is a string which is same when we read it forward & backward.
# Eg - "madam", "racecar" etc.
# [Hint - A palindrome string is equal to the reversed version of the string.
#  We can use a loop to reverse the string manually.]
string = input("Enter a string : ")
if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")