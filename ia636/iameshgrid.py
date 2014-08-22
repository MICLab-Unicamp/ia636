# -*- encoding: utf-8 -*-
# Module iameshgrid

from numpy import *

def iameshgrid(vx, vy):

    x = resize(vx, (len(vy), len(vx)))
    y = transpose(resize(vy, (len(vx), len(vy))))
    return x, y

