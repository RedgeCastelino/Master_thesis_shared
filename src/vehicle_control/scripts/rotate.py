import math

def rotate (x,y,angle):

    rotx = x * math.cos(angle) - y * math.sin(angle)
    roty = x * math.sin(angle) + y * math.cos(angle)

    return [rotx,roty]
