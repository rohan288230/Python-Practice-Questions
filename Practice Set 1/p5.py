# Q5. Profit / Loss
# Cost Price aur Selling Price input lo.
# - SP > CP → "Profit"
# - SP < CP → "Loss"
# - SP == CP → "No Profit No Loss"
cp = int(input("Enter Cost Price : "))
sp = int(input("Enter Selling Price : "))
if sp > cp :
    print("Profit")
elif sp < cp :
    print("Loss")
else:
    print("No Profit No Loss")