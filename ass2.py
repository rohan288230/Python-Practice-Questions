# Problem Statement:
# You work in XYZ Corporation as a Data Analyst. Your company has told you 
# to work with the if-else condition.
# Tasks To Be Performed:
# 1. Take three user inputs and print the greatest number from those inputs
# using if-else condition. Edge cases, if any, should also be handled.
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
if (a>=b) and (a>=c):
    print("Greatest number is ",a)
elif(b>=a) and (b>=c):
    print("Greatest number is ",b)
else:
    print("Greatest number is ",c)