# -*- encoding: utf-8 -*-
# Module iarot90

from numpy import *

def iarot90(img, axis='X'):

   from ia636 import iaffine
   PIVAL = math.pi

   g = 0

   if axis == 'X':
      Trx = array([[cos(PIVAL/2), -sin(PIVAL/2), 0, img.shape[1] - 1],
                   [sin(PIVAL/2),  cos(PIVAL/2), 0, 0],
                   [           0,             0, 1, 0],
                   [           0,             0, 0, 1]]).astype(float)
      g = iaffine(img, Trx, [img.shape[1], img.shape[0], img.shape[2]])

   elif axis == 'Y':
      Try = array([[ cos(PIVAL/2), 0, sin(PIVAL/2), 0],
                    [            0, 1,            0, 0],
                    [-sin(PIVAL/2), 0, cos(PIVAL/2), img.shape[0] - 1],
                    [            0, 0,            0, 1]])
      g = iaffine(img, Try, [img.shape[2], img.shape[1], img.shape[0]])
   elif axis == 'Z':
      Trz = array([[1,            0,             0, 0],
                    [0, cos(PIVAL/2), -sin(PIVAL/2), img.shape[2] - 1],
                    [0, sin(PIVAL/2),  cos(PIVAL/2), 0],
                    [0,            0,             0, 1]]).astype(float)
      g = iaffine(img, Trz, [img.shape[0], img.shape[2], img.shape[1]])

   return g

