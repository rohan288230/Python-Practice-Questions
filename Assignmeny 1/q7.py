# Ask the user for a temperature in Celsius(string input).
# Convert it to float, then calculate and print temperature in Fahrenheit.
# conversion formula: Fahrenheit Temp = (Celsius Temp*(9/5))+32
celsius = input("Enter temperature in Celsius : ")
celsius = float(celsius)
fahrenheit = (celsius * (9/5)) + 32
print("Temperature in Fahrenheit is ", fahrenheit)