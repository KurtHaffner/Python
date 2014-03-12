import random

def montePI(n):
    hit = 0
    miss = 0
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 <= 1:
            hit = hit + 1

        else:
            miss = miss + 1

    print ("The estimation of PI using", n, "dart throws is: ", (hit/(n/4)))
