# Q18. Stock Check
# Input lo:
# is_out_of_stock = True/False

# Agar product out of stock nahi hai, print:
# "Product Available"
# Otherwise:
# "Out of Stock"
is_out_of_stock = input("Is product out of stock ? True/False ")
is_out_of_stock = is_out_of_stock.lower() == "true"
if not is_out_of_stock:
    print("Product Available")
else:
    print("Out of stock.")