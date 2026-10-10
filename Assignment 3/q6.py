# Q6. Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to length.
# Example:
# {"apple": 5, "banana":6, .....}
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dictionary = {}
for fruits in words:
    dictionary[fruits] = len(fruits)
print(dictionary) 