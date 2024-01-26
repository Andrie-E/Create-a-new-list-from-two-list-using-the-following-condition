# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# pseudocode

# create the function
def create_new_list(list1, list2):
    new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
    return new_list

# provide the list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# print the result
result = create_new_list(list1, list2)
print(result)


