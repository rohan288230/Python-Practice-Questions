# Take a decimal number as input (like 45.78) and output its:
#     - integral part - 45
#     - fractional part - .78
num = float(input("Enter a decimal number : "))
integral = int(num)
fractional = num - integral
print("Integral part = ", integral)
print("Fractional part = ", round(fractional,2))