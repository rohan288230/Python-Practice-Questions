# Q7. Design a program to continuously input a number n from user & 
# print if it is positive or negative until the user enters "Quit".
while True:
    num = input("Enter a number : (or Quit to stop)")
    if num.lower() == "quit":
        print("Program Stopped")
        break
    num = int(num)
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("zero")