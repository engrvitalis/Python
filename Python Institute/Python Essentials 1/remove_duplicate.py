# This program removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not 
# more than once.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []
#
# Write your code here.
#
for element in my_list:
    if element not in temp_list:
        temp_list.append(element)

my_list = temp_list[:]
del temp_list

print("The list with unique elements only:")
print(my_list)
