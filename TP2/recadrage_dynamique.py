import cv2
import numpy as np

im1 = cv2.imread('ressources/Ihistdyn.png', cv2.IMREAD_GRAYSCALE)
im1 = np.array(im1)

imgHeight = np.size(im1, 0)
imgWidth = np.size(im1, 1)
print(imgWidth)
result = np.zeros((imgHeight,imgWidth))
result = np.ascontiguousarray(result, dtype=np.uint8)

a = np.min(im1)
b = np.max(im1)

maxPixelValue = 255

for row in range(imgHeight):
  for pixel in range(imgWidth):
    pixelValue = im1[(row,pixel)]
    result[(row, pixel)]= round(maxPixelValue*(pixelValue-a)/(b-a))

cv2.imwrite('recadrage_dynamique.png',result)
