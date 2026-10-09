# Q10. Let's create a "Number Guessing Game".
# Given a secret number (already decided by you),
# write a program that asks the user to guess it and prints:
# - "Too high" if the guess is above the number
# - "Too low" if the guess is below
# - "Correct!" if the guess matches
num = int(input("Enter a number : "))
if num > 100 :
    print("Too High")
elif num < 100:
    print("Too Low")
else:
    print("Correct !")