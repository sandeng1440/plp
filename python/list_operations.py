# making an empty list
my_list = []

# adding 10, 20, 30, 40 to the end to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting 15 in the second position
my_list.insert(1, 15)

# merging two lists
my_list.extend([50, 60, 70])

# removing the last element
my_list.pop()

# sorting in ascending order
my_list.sort()

# getting the index of 30
print(f"{my_list.index(30) = }")
