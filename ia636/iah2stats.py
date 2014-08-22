# -*- encoding: utf-8 -*-
# Module iah2stats

def iah2stats(h):
    import numpy as np
    import ia636 as ia

    hn = 1.0*h/h.sum() # compute the normalized image histogram
    v = np.zeros(11) # number of statistics

    # compute statistics
    n = len(h) # number of gray values
    v[0]  = np.sum((np.arange(n)*hn)) # mean
    v[1]  = np.sum(np.power((np.arange(n)-v[0]),2)*hn) # variance
    v[2]  = np.sum(np.power((np.arange(n)-v[0]),3)*hn)/(np.power(v[1],1.5))# skewness
    v[3]  = np.sum(np.power((np.arange(n)-v[0]),4)*hn)/(np.power(v[1],2))-3# kurtosis
    v[4]  = -(hn[hn>0]*np.log(hn[hn>0])).sum() # entropy
    v[5]  = np.argmax(h) # mode
    v[6:]  = ia.iah2percentile(h,np.array([1,10,50,90,99])) # 1,10,50,90,99% percentile
    return v

