import cv2
import numpy as np

im1 = cv2.imread('egalisation.png', cv2.IMREAD_GRAYSCALE)
im1 = np.array(im1)

histoHeight = np.size(im1, 0)
print(histoHeight)
histoWidth = 255
histo = []
result = np.full((histoHeight,histoWidth),255)
result = np.ascontiguousarray(result, dtype=np.uint8)

for i in range(255):
  count = np.count_nonzero(im1==i)
  histo.append(count)

histoMax = np.max(histo)

for index, pixelValue in enumerate(histo):
  cv2.line(result, (index,histoHeight-2), (index,histoHeight-int(pixelValue*histoHeight/histoMax)), (0,0,0), 1)
  result[histoHeight-1][index]=index
  result[histoHeight-2][index]=0

cv2.imwrite('histo_egalisation.png',result)