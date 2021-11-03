import cv2
import numpy as np

im = cv2.imread('ressources/Ibin.png', cv2.IMREAD_GRAYSCALE)

im = np.array(im)

structuringElement = np.array([[0,1,0],[1,1,1],[0,1,0]],np.uint8)
filteredImage = cv2.dilate(im,structuringElement)
cv2.imwrite("dilated.png", filteredImage)