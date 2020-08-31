import math
import numpy as np

def rotate (x,y,angle):

    rot= np.zeros((2,2))
    rot[0,0] = math.cos(angle)
    rot[0,1] = -(math.sin(angle))
    rot[1,0] = math.sin(angle)
    rot[0,1]= math.cos(angle)
    pos = [x,y]
    pos = rot.dot(pos)
    rotx=  pos[0,0]
    roty= pos[1,0]
    #rotx = x * math.cos(angle) - y * math.sin(angle)
    #roty = x * math.sin(angle) + y * math.cos(angle)

    return [rotx,roty]
