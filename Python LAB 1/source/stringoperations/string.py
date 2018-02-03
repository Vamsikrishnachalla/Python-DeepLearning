import math

# function to find the longest word and also printing the reverse of each word in the string
def stringoperations(stringlist,stringinput):

    # operating the string to print the longest word

    # initializing an object to find the longest word
    reqword = ''

    # searching for the longest word in whole list
    for word in stringlist:

        # Comparing the lengths of every word among the set to find the longest one
        if len(word) > len(reqword):
            reqword = word
    print ('The longest word in the string is:', reqword)

    # operating on the string to print the reverse of the words in the string

    # reversing the words and storing them into a list at a time
    reversewords = [rev[::-1] for rev in stringlist]

    # Joining the reversed words into a sentence
    revsentence = " ".join(reversewords)

    # Printing the new sentence that is reversed
    print('The reversed sentence is:', revsentence)


    # Finding the middle words in the string

    # Loading the length of the list into a variable
    length = len(stringlist)

    # If the number of words in the list are even, then we will have two middle words.
    # If the number of words in the list are odd, then we will have one middle word.

    # Checking if the string length is even or odd and then printing the middle words in the sentence.
    if (length%2 == 0):
        mid = int(length/2)
        # Printing the middle words if the number of words are even
        print(' The middle words are:', stringinput.split(" ")[mid], stringinput.split(" ")[mid-1])

    else:
        mid = int(length/2)
        # Printing the middle word if the number of words are odd
        print('The middle word is:', stringinput.split(" ")[mid])


# entering the string as input to perform verious operations
stringinput = input("Enter the string on which you want to perform string operations:")

# Splitting the sentence into individual words
stringlist = stringinput.split()

# Calling the function to perform various operations on the string
stringoperations(stringlist,stringinput)
