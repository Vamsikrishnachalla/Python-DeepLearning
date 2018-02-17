# Importing numpy package to perform random picking of numbers and other operations on it
import numpy as n
# Initializing a variable to store 15 random integers between the range of 0-20
ran = n.random.randint(20,size=15)
print(" The randomly picked integers are:", "\n", ran)
# Counting the number of occurrences of each randomly picked integer
count=n.bincount(ran)
# Printing the number with maximum occurrences
print("The number with maximum number of occurrences:", n.argmax(count))

