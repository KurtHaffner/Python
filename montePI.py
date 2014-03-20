#Import random for the random numbers.
import random

#Function that will be called.
def montePI(n):
    
    #Define hit and miss to keep track of the hits and misses.
    hit = 0
    miss = 0

    #For loop that will run the test however many times
    #the user specifies.
    for i in range(n):

        #Get x and y coordinates by choosing a random number
        #from -1 to 1, including decimals.
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        #If the dart location is within the circle, count it
        #as a hit.
        if x**2 + y**2 <= 1:
            hit = hit + 1

        #Else, count it as a miss.
        else:
            miss = miss + 1

    #Print the number of dart throws and then do the
    #math to show the estimation of PI.
    print ("The estimation of PI using", n, "dart throws is: ", (hit/(n/4)))
