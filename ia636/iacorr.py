# -*- encoding: utf-8 -*-
# Module iacorr

def iacorr(X, Y):
    import numpy as np

    if X.size == Y.size:
        X = X.ravel()
        Y = Y.ravel()

        Xm = X.mean()
        Ym = Y.mean()
        Xc = X - Xm
        Yc = Y - Ym
        cov = (Xc*Yc).mean()
        v1 = (Xc*Xc).mean()
        v2 = (Yc*Yc).mean()
    else:

        if Y.ndim == (X.ndim + 1):
            # m is the number of pixels of X
            n = Y.shape[0]              # number of images in Y
            X = X.ravel().reshape(1,-1) # shape (1,m)
            Y = Y.reshape(n,-1)         # shape (n,m)

            Xm = X.mean()                     # scalar
            Ym = Y.mean(axis=1,keepdims=True) # shape (n,1)
            Xc = X - Xm                       # shape (1,m)
            Yc = Y - Ym                # broadcast  shape (n,m)-(n,1) -> (n,m)
            cov = (Xc*Yc).mean(axis=1) # broadcast  shape (1,m)*(n,m) -> (n,)
            v1 = (Xc*Xc).mean()        # scalar
            v2 = (Yc*Yc).mean(axis=1)  # reduction (n,m) -> (n,)

    return cov/(np.sqrt(v1*v2))

