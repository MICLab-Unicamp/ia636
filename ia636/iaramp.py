# -*- encoding: utf-8 -*-
# Module iaramp

from numpy import *

def iaramp(s, n, range=[0,255]):
    aux = array(n)
    s_orig = s

    if len(aux.shape) == 0:
        s = [1,s[0],s[1]]
        n = [0,0,n]
        range = [0,0,0,0,range[0],range[1]]

    slices,rows, cols = s[0], s[1], s[2]
    z,y,x = indices((slices,rows,cols))
    gz = z*n[0]/slices * (range[1]-range[0]) / (n[0]-1) + range[0]
    gy = y*n[1]/rows * (range[3]-range[2]) / (n[1]-1) + range[2]
    gx = x*n[2]/cols * (range[5]-range[4]) / (n[2]-1) + range[4]
    return (gz+gy+gx).reshape(s_orig)

