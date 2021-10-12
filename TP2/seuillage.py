import cv2
import numpy as np

im1 = cv2.imread('ressources/otsu/otsu4.png', cv2.IMREAD_GRAYSCALE)
im1 = np.array(im1)

imgHeight = np.size(im1, 0)
imgWidth = np.size(im1, 1)
print(imgWidth)
result = np.zeros((imgHeight,imgWidth))
result = np.ascontiguousarray(result, dtype=np.uint8)

seuil = 124

for row in range(imgHeight):
  for pixel in range(imgWidth):
    pixelValue = im1[(row,pixel)]
    if(pixelValue>=seuil):
      result[(row, pixel)]=pixelValue

cv2.imwrite('otsu4_seuillee_methode_otsu.png',result)
