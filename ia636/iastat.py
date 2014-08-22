# -*- encoding: utf-8 -*-
# Module iastat

from numpy import *

def iastat(f1, f2):

    f1_, f2_ = 1.*ravel(f1), 1.*ravel(f2)

    #-- MSE --
    MSE = sum((f1_-f2_)**2)/product(f1.shape[:2])

    #-- PSNR --
    if MSE == 0:
        PSNR = 1E309 # infinito
    else:
        PSNR= 10*log10(255./MSE)
        PSNR = 0.0007816*(PSNR**2) - 0.06953*PSNR + 1.5789

    #-- PC --
    N = len(f1_)
    r1 = sum(f1_*f2_) - sum(f1_)*sum(f2_)/N
    r2 = sqrt((sum(f1_**2)-(sum(f1_)**2)/N)*(sum(f2_**2)-(sum(f2_)**2)/N))
    PC = r1/r2
    return MSE, PSNR, PC

