# -*- encoding: utf-8 -*-
# Module iapca

import numpy as np

def iapca(X):

    n, dim = X.shape
    mu = X.mean(axis=0)
    X = X - mu

    C = (X.T).dot(X)/(n-1)        # Covariance matrix
    e,V = np.linalg.eigh(C)       # eigenvalues and eigenvectors of the covariance matrix
    indexes = np.argsort(e)[::-1] # sorting eigenvalues from largest
    e  = e [indexes]              # update e and V
    V = V[:,indexes]
    return V,e,mu

