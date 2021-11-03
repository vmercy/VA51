import cv2
import numpy as np

im = cv2.imread('ressources/Ibin.png', cv2.IMREAD_GRAYSCALE)

im = np.array(im)

structuringElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
filteredImage = cv2.dilate(im,structuringElement)
filteredImage = cv2.erode(im,structuringElement)
cv2.imwrite("fermeture.png", filteredImage)