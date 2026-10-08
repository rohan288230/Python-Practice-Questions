# Ask the user for: Principal(P), Rate(R), Time(T).
# Convert all to float and compute simple interest.
# SI = (P*R*T)/100
P = float(input("Enter Principal : "))
R = float(input("Enter Rate : "))
T = float(input("Enter Time : "))
SI = (P*R*T)/100
print("The simple interest is ",SI)