# Q14. BMI Calculator: Weight aur height se BMI calculate karo. 
# Zero ya negative height reject karo.
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meter : "))
if height <=0:
    print("Invalid height")
elif weight <= 0:
    print("Invalid weight")
else:
    bmi = weight/(height**2)
    print(f"Your BMI is : {bmi:.2f}")