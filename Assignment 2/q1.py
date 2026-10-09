# Q1. Write a program that takes salary as input.
# Using conditional statements, calculate the
# final tax rate based on these rules:
# - if salary < 30,000 - 5%
# - if salary 30000 - 70000 - 15%
# - if salary > 70000 - 25%
salary = int(input("Enter your salary : "))
if salary < 30000 :
    tax = 5 
elif salary <= 70000 :
    tax = 15
else :
    tax = 25
final_tax = (salary * tax)/100
print("The final tax rate : ",final_tax)