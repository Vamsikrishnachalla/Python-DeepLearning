# Program To Find Triplets that sum up to Zero From the given set  of integers
def findTriplets( Array, size ):
    found = True
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(0, size-2):

        # for the first number a[i]
        num1 = Array[i]

        for j in range( i+1, size-1 ):

            # for the second number a[j]
            num2 = Array[j]

            for k in range( i+3, size ):

                # for the third number a[k]
                num3 = Array[k]
                sum= num1 + num2 + num3

                # checking if the sum is equal to zero
                if ( sum == 0 ):
                    print( "triplets are", Array[i], Array[j], Array[k])
                    found = True

    if ( found == False ):
        print(" Triplets does not exist ")


# Defining the array and it's elements
Array = [1, 2, 3, -3, -5, 0, 8]

# Finding out the length of the array

size = len(Array)
sum = 0

# Calling the function to find the triplets that sum up to 0
findTriplets( Array, size )


