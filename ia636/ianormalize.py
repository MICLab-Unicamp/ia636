# -*- encoding: utf-8 -*-
# Module ianormalize

from numpy import *

def ianormalize(f, range=[0,255]):

    f = asarray(f)
    range = asarray(range)
    if f.dtype.char in ['D', 'F']:
        raise Exception, 'error: cannot normalize complex data'
    faux = ravel(f).astype(float)
    minimum = faux.min()
    maximum = faux.max()
    lower = range[0]
    upper = range[1]
    if upper == lower:
        g = ones(f.shape) * maximum
    if minimum == maximum:
        g = ones(f.shape) * (upper + lower) / 2.
    else:
        g = (faux-minimum)*(upper-lower) / (maximum-minimum) + lower
    g = reshape(g, f.shape)

    if f.dtype == uint8:
        if upper > 255:
            raise Exception,'ianormalize: warning, upper valuer larger than 255. Cannot fit in uint8 image'
    g = g.astype(f.dtype) # set data type of result the same as the input image
    return g

