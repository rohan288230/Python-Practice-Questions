# The user enters a string containing a number (e.g., "45"). Convert it to
# an integer
# a float
# a string again
# Print all three values with their types.
a = input("Enter a number : ")
integer_value = int(a)
float_value = float(a)
string_value = str(a)
print("The integer value", integer_value, type(integer_value))
print("The float value", float_value, type(float_value))
print("The string value", string_value, type(string_value))