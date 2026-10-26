# Q20. Financial Summary: Income, expenses aur savings rate calculate karo.
# Zero income aur negative amounts handle karo.
income = int(input("Enter your income : Rs. "))
expenses = int(input("Enter your expenses : Rs. "))
if income < 0 or expenses < 0:
    print("Invalid : Income and expenses cannot be negative.")
elif income == 0:
    print("Invalid : Income must be greater than 0.")
else :
    saving = income - expenses
    saving_rate = (saving/income)*100
    print(f"Saving : {saving:.2f}")
    print(f"Saving rate : {saving_rate:.2f}")