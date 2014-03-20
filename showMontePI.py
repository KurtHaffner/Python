#Import random for randoms and turtle for drawing.
import random
import turtle

def showMontePI(n):

    #Make a turtle for the dart throws.
    #Will also draw the grid.
    dart = turtle.Turtle()
    dart.screen.title('Monte Carlo PI Simulation')#Set screen title.
    dart.screen.setworldcoordinates(-2,-2,2,2)#Set view to 2X2 square.
    dart.hideturtle()#Hide the turtle so it looks nice.

    #Draw the coordinate system lines.
    dart.forward(2)
    dart.backward(4)
    dart.home()
    dart.left(90)
    dart.forward(2)
    dart.backward(4)
    dart.home()
    dart.penup()

    #Set the speed to 1000, just to make it a bit faster.
    dart.speed(1000)

    #Set hit and miss, for hits and misses.
    hit = 0
    miss = 0

    #For loop that runs the test.
    for i in range(n):

        #X and Y coordinates set to a random number, -1 to 1.
        #Includes decimals.
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        #If the dart is in the circle, count it as a hit.
        if x**2 + y**2 <= 1:
            hit = hit + 1

            #Go to the dart location and make a blue dot.
            dart.goto(x,y)
            dart.color('blue')
            dart.dot(.01)

        #Else count it as a miss.
        else:
            miss = miss + 1

            #Go to the dart location and make a red dot.
            dart.goto(x,y)
            dart.color('red')
            dart.dot(.01)

    #Print out the number of throws and do the math for
    #the estimation of PI.
    print ("The estimation of PI using", n, "dart throws is: ", (hit/(n/4)))
