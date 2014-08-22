# -*- encoding: utf-8 -*-
# Module iatiling

import numpy as np
def iatiling(f, w):
  H = Hold = w
  g = np.zeros((H,w),'uint8')
  ih = iw = 0
  himax = 0
  for i in range(len(f)):
    hi,wi = f[i].shape
    if iw+wi > w:  # test if reach width
      iw = 0
      ih += himax + 1
      himax = 0
    if ih+hi > H:  # at any time test if reach height
      H += w
      g1 = np.zeros((H,w),'uint8')
      g1[:Hold,:] = g
      g = g1
      Hold = H
    g[ih:ih+hi, iw:iw+wi] = f[i] # insert another image
    iw += wi + 1
    himax = max(himax,hi)
  return g

