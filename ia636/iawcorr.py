# -*- encoding: utf-8 -*-
# Module iawcorr

def iawcorr(im1, im2, w):
    import numpy as np
    w = w.astype(float)
    wf = w.ravel()
    sw = np.sum(wf)
    im1f = im1.astype(float).ravel()
    im2f = im2.astype(float).ravel()
    mim1f = np.sum(im1f * wf)/sw
    mim2f = np.sum(im2f * wf)/sw

    im1x = im1f - mim1f
    im2x = im2f - mim2f

    cov12 = np.sum(im1x*im2x*wf)/sw
    cov11 = np.sum(im1x*im1x*wf)/sw
    cov22 = np.sum(im2x*im2x*wf)/sw

    return cov12/np.sqrt(cov11*cov22)

