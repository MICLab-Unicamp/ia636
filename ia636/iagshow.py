# -*- encoding: utf-8 -*-
# Module iagshow

import numpy as np

def iagshow(X, X1=None, X2=None, X3=None, X4=None, X5=None, X6=None):

    if X.dtype == np.bool: X = np.where(X,255,0).astype('uint8')
    r = X
    g = X
    b = X
    if X1 is not None: # red 1 0 0
      if (X1.dtype != np.bool): raise Exception,'X1 must be binary overlay'
      r = np.where(X1,255,r)
      g = np.where(~X1,g,0)
      b = np.where(~X1,b,0)
    if X2 is not None: # green 0 1 0
      if (X2.dtype != np.bool): raise Exception,'X2 must be binary overlay'
      r = np.where(~X2,r,0)
      g = np.where(X2,255,g)
      b = np.where(~X2,b,0)
    if X3 is not None: # blue 0 0 1
      if (X3.dtype != np.bool): raise Exception,'X3 must be binary overlay'
      r = np.where(~X3,r,0)
      g = np.where(~X3,g,0)
      b = np.where(X3,255,b)
    if X4 is not None: # magenta 1 0 1
      if (X4.dtype != np.bool): raise Exception,'X4 must be binary overlay'
      r = np.where(X4,255,r)
      g = np.where(~X4,g,0)
      b = np.where(X4,255,b)
    if X5 is not None: # yellow 1 1 0
      if (X5.dtype != np.bool): raise Exception,'X5 must be binary overlay'
      r = np.where(X5,255,r)
      g = np.where(X5,255,g)
      b = np.where(~X5,b,0)
    if X6 is not None: # cyan 0 1 1
      if (X6.dtype != np.bool): raise Exception,'X6 must be binary overlay'
      r = np.where(~X6,r,0)
      g = np.where(X6,255,g)
      b = np.where(X6,255,b)
    return np.array([r,g,b])

