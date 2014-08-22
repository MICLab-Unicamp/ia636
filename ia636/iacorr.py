# -*- encoding: utf-8 -*-
# Module iacorr

def iacorr(im1, im2):
    import numpy as np
    avim1 = np.average(im1.astype(float).flat)
    avim2 = np.average(im2.astype(float).flat)

    im1x = im1.astype(float) - avim1
    im2x = im2.astype(float) - avim2

    cov = np.average(im1x*im2x)
    v1 = np.average(im1x*im1x)
    v2 = np.average(im2x*im2x)

    return cov/(np.sqrt(v1*v2))

