# 9. Temperature Converter: Celsius ko Fahrenheit aur 
# Kelvin mein convert karo. Decimal precision maintain karo.
celsius_temp = float(input("Enter temp(in Celsius) : "))

kelvin_temp = celsius_temp + 273.15
fahrenheit_temp = (celsius_temp * 9/5) + 32
print("Temperature in Fahrenheit : ",fahrenheit_temp)
print("Temperature in Kelvin : ",kelvin_temp)