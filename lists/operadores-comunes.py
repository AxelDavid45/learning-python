my_list = [8.4, 9, 10, 2.2]

mini = min(my_list)
# Returns the lowest value in a list
print("The lowest value in the list is: " + str(mini))
# Return the highest value
highest = max(my_list)
print("The highest value in the list is: " + str(highest))
# Return the position of an element
pos = my_list.index(2.2)
print("The position of 2.2 is: " + str(pos))
# Count the match of an element in a list
match = my_list.count(2.2)
print(match)
# return the lenght of a list
print(len(my_list))

