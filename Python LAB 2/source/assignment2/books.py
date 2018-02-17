# Declaring the list with book names as keys and cost of books as values
bookdictionary = dict([("python and deep learning",50),("Web development",60),("Design and analysis of algorithms",55),("Data base management systems",65),("android development",68),("Deep Learning",70)])
print("Now let us have glance at all the list of books in the UMKC book store:")
# Printing all the books in the bookstore and their costs
for key,values in bookdictionary.items():
    print(key,values)
# Specifying the range of costs  that we want to look for:
print("Now enter the range of values to find the books in that range")
# Taking the start value as input
startval = int(input("enter the starting value:"))
# Taking the last value as input
lastval = int(input("enter the ending value:"))
# Searching over the whole list for the books that fall in the given range of costs
print("The books available in the Umkc BookStore that are in the given range are:")
for bname,value in bookdictionary.items():
    if value >= startval and value <= lastval:
        print(bname)
