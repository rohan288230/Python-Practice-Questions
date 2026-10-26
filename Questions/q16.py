# Q16. Unit Converter: Kilometers ko meters, centimeters aur miles 
# mein convert karo using separate conversion variables.
km = float(input("Enter distance (in km) : "))
m = km * 1000
cm = m * 100
miles = km / 1.609
print(f"Distance (in m) : {m}")
print(f"Distance (in cm) : {cm}")
print(f"Distance (in miles) : {miles}")