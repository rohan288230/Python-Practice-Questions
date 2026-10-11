# Q8. Temperature
# Temperature input lo:
# - = 40 → "Very Hot"
# - = 30 → "Hot"
# - = 20 → "Normal"
# - = 10 → "Cold"
# - Below 10 → "Very Cold"
temp = int(input("Enter Temperature : "))
if temp >=40:
    print("Very Hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Normal")
elif temp >= 10:
    print("Cold")
else:
    print("Very Cold")