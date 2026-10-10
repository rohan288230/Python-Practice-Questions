# # Create a dictionary where:
# # - Keys = student names
# # - values = marks(integer)
# # Write a menu-based program where user presses a key ('A','B','C','D')
# # depending on the operation they want to perform on the dictionary.
# # 1. A - Add a student 
# # 2. B - Update marks
# # 3. C - Search for a student 
# # 4. D - Display all students and marks
students = {}
while True:
    choice = input("\n A - Add \n B - Update \n C - Search \n D = Display \n E - Exit\n").upper()
    if choice == "A":
        name = input("Enter name : ")
        marks = int(input("Enter marks : "))
        students[name] = marks
    elif choice == "B":
        name = input("Enter name : ")
        if name in students:
            students[name] = int(input("Enter new marks : "))
        else:
            print("Student not found")
    elif choice == "C":
        name = input("Enter name : ")
        print(students.get(name,"Student nor found"))
    elif choice == "D":
        print(students)
    elif choice == "E":
        break
    else:
        print("Invalid Choice")