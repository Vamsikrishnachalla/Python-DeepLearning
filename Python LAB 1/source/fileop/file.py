# List1 in which students list of python class are stored in:
list1 = ['Vamsi Challa', 'Rajesh', 'Mahesh', 'Krishna', 'Roshan', 'Sudheer', 'Yeshwanth', 'Rahul', 'Sampath']

# List2 in which students list of web development class are stored in:
list2 = ['Vamsi Challa', 'Srinivas', 'Girish', 'Dinesh', 'Suhas', 'Pruthvi', 'Sudheer', 'Rahul', 'Yeshwanth', 'Bhavani Prasad']

# Comparing both the files to print common students in both the classes
print(" Comparing both the files starts:")
print('. . . . .  . . . .  \n ')

# Printing students who are common in both the classes
print("Students who are common in both python and web developement classes are: \n")
for c in list1:
    if c in list2:
        print(c)
print('\n')

# Printing Students who are not common in both classes
print("Students who have taken only one of web development or python are: \n")

# Picking out the odd one's out from  the first list
for d in list1:
    if d not in list2:
        print(d)

# Picking out the odd one's out from the second list
for e in list2:
    if e not in list1:
        print(e)





