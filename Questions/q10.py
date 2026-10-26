# 10. Salary Calculator: Monthly salary aur bonus percentage 
# se annual salary calculate karo.
monthly_salary = float(input("Enter monthly salary : "))
bonus_percentage = float(input("Enter bonus : "))
annual_salary = monthly_salary * 12
bonus = annual_salary * bonus_percentage/100
total_salary = annual_salary + bonus
print(f"Annual salary : {annual_salary:.2f}")
print(f"Bonus : {bonus:.2f}")
print(f"Total annual salary : {total_salary:.2f}")