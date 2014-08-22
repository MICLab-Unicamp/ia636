# -*- encoding: utf-8 -*-
# Module iainterpollin

def iainterpollin(f, pts):
    # f - one, two or three dimention array
    # pts - array of points to interpolate:
    # throws IndexError if there are indices out of range in pts
    from iainterpollin import iainterpollin1D, iainterpollin2D, iainterpollin3D
    import numpy as np
    f = f.astype(float)
    if f.ndim == 1:
        return iainterpollin1D(f, np.ravel(pts))
    if f.ndim == 2:
        return iainterpollin2D(f, pts)
    if f.ndim == 3:
        return iainterpollin3D(f, pts)

def iainterpollin1D(f, pts):
    # f - one dimention array
    # pts - array of points to interpolate:
    # throws IndexError if there are indices out of range in pts
    import numpy as np

    # integer indices
    ipts = np.floor(pts).astype(int)

    # fractional indices
    fpts = pts - ipts

    # workaround for the case some index equals the last valid index
    fpts[ipts>=f.shape[0]-1] += 1
    ipts[ipts>=f.shape[0]-1] -= 1

    I = ipts.copy()
    Ix = ipts.copy()+1

    a = f[I]
    b = f[Ix] - a

    return a + b*fpts


def iainterpollin2D(f, pts):
    # f - bi-dimentional image
    # pts - array (2xN) of points to interpolate:
    # throws IndexError if there are indices out of range in pts
    # let's consider x the first and y the second dimention
    import numpy as np

    # integer indices
    ipts = np.floor(pts).astype(int)

    # fractional indices
    fpts = pts - ipts

    # workaround for the case some index equals the last valid index in the respective dimension
    fpts[0][ipts[0]>=f.shape[0]-1] += 1
    ipts[0][ipts[0]>=f.shape[0]-1] -= 1
    fpts[1][ipts[1]>=f.shape[1]-1] += 1
    ipts[1][ipts[1]>=f.shape[1]-1] -= 1

    I = ipts.copy()
    Ix = ipts.copy()
    Ix[0] += 1
    Iy = ipts.copy()
    Iy[1] += 1
    Ixy = Ix.copy()
    Ixy[1] += 1

    a = f[I[0], I[1]]
    b = f[Ix[0], Ix[1]] - a
    c = f[Iy[0], Iy[1]] - a
    e = f[Ixy[0], Ixy[1]] - a - b - c

    return a + b*fpts[0] + c*fpts[1] + e*fpts[0]*fpts[1]


def iainterpollin3D(ff, pts):
    # ff - tri dimentional image
    # pts - array (3xN) of points to interpolate:
    # throws IndexError if there are indices out of range in pts
    # let's consider x the first dimension, y the second and z the third
    import numpy as np

    # integer indices
    ipts = np.floor(pts).astype(int)

    # fractional indices
    fpts = pts - ipts

    # workaround for the case some index equals the last valid index in the respective dimension
    fpts[0][ipts[0]>=ff.shape[0]-1] += 1
    ipts[0][ipts[0]>=ff.shape[0]-1] -= 1
    fpts[1][ipts[1]>=ff.shape[1]-1] += 1
    ipts[1][ipts[1]>=ff.shape[1]-1] -= 1
    fpts[2][ipts[2]>=ff.shape[2]-1] += 1
    ipts[2][ipts[2]>=ff.shape[2]-1] -= 1

    I = ipts.copy()
    Ix = ipts.copy()
    Ix[0] += 1
    Iy = ipts.copy()
    Iy[1] += 1
    Iz = ipts.copy()
    Iz[2] += 1
    Ixy = Ix.copy()
    Ixy[1] += 1
    Ixz = Ix.copy()
    Ixz[2] += 1
    Iyz = Iy.copy()
    Iyz[2] += 1
    Ixyz = Ixy.copy()
    Ixyz[2] += 1

    a = ff[I[0], I[1], I[2]]
    b = ff[Ix[0], Ix[1], Ix[2]] - a
    c = ff[Iy[0], Iy[1], Iy[2]] - a
    d = ff[Iz[0], Iz[1], Iz[2]] - a
    e = ff[Ixy[0], Ixy[1], Ixy[2]] - a - b - c
    f = ff[Ixz[0], Ixz[1], Ixz[2]] - a - b - d
    g = ff[Iyz[0], Iyz[1], Iyz[2]] - a - c - d
    h = ff[Ixyz[0], Ixyz[1], Ixyz[2]] - a - b - c - d - e - f - g

    return a + b*fpts[0] + c*fpts[1] + d*fpts[2] + e*fpts[0]*fpts[1] + f*fpts[0]*fpts[2] + g*fpts[1]*fpts[2] + h*fpts[0]*fpts[1]*fpts[2]

