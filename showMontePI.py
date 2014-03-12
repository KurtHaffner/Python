import random
import turtle

def showMontePI(n):
    dart = turtle.Turtle()
    dart.screen.title('Monte Carlo PI Simulation')
    dart.screen.setworldcoordinates(-2,-2,2,2)
    dart.hideturtle()

    dart.forward(2)
    dart.backward(4)
    dart.home()
    dart.left(90)
    dart.forward(2)
    dart.backward(4)
    dart.home()
    dart.penup()

    dart.speed(1000)

    hit = 0
    miss = 0
    
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 <= 1:
            hit = hit + 1

            dart.goto(x,y)
            dart.color('blue')
            dart.dot(.01)

        else:
            miss = miss + 1

            dart.goto(x,y)
            dart.color('red')
            dart.dot(.01)

    print ("The estimation of PI using", n, "dart throws is: ", (hit/(n/4)))
