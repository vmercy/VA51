import cv2
import numpy as np

im1 = cv2.imread('ressources/route1.png', cv2.IMREAD_GRAYSCALE)
im1 = np.array(im1)
im2 = np.zeros(im1.shape)

pixelValue = im1[250,226]

for indexI, i in enumerate(im1):
  for indexJ, j in enumerate(i):
    if abs(j-pixelValue)<20:
      im2[indexI,indexJ]=255

cv2.imwrite('seuille.png',im2)

