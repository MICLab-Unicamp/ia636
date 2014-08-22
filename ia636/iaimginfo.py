# -*- encoding: utf-8 -*-
# Module iaimginfo

import numpy as np

def iaimginfo(f):
    t = type(f)
    if t != np.ndarray:
        return 'Not a ndarray. It is %s' % (t,)
    else:
        dt = f.dtype
        if dt == 'bool':
            return '%s %s %s %s %s' % (t, np.shape(f), f.dtype, f.min(), f.max())
        elif dt == 'uint8':
            return '%s %s %s %d %d' % (t, np.shape(f), f.dtype, f.min(), f.max())
        else:
            return '%s %s %s %f %f' % (t, np.shape(f), f.dtype, f.min(), f.max())

