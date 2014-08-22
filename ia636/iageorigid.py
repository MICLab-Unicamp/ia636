# -*- encoding: utf-8 -*-
# Module iageorigid

from numpy import *

def iageorigid(f, scale, theta, t):
    from iaffine import iaffine

    Ts   = [[scale[1],0,0], [0,scale[0],0], [0,0,1]]
    Trot = [[cos(theta),-sin(theta),0], [sin(theta),cos(theta),0], [0,0,1]]
    Tx   = [[1,0,t[1]], [0,1,t[0]], [0,0,1]]
    g = iaffine(f, dot(dot(Tx,Trot), Ts))
    return g

