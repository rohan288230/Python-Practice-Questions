# Q15. Percentage Report: Obtained marks aur maximum marks se 
# percentage calculate karo. Zero maximum marks handle karo.
obtained_marks = int(input("Enter your obtained marks : "))
maximum_marks = int(input("Enter your maximum marks : "))
if maximum_marks <= 0:
    print("Invalid Maximum Marks")
elif obtained_marks < 0 or obtained_marks > maximum_marks :
    print("Invalid Obtained Marks")
else:
    percentage = (obtained_marks/maximum_marks)*100
    print(f"Percentage : {percentage}%")