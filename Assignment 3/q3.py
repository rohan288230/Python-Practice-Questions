# Q3. Input two lists of integer from the user. 
# Merge them into one list and sort the result.
list1 = list(map(int , input("Enter numbers : ").split()))
list2 = list(map(int , input("Enter numbers : ").split()))
merged_list = list1 + list2
merged_list.sort()
print("The merged and sorted list is : ", merged_list)