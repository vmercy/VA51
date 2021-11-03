from scipy import signal
import cv2
import numpy as np

im = cv2.imread('ressources/I2filter.png', cv2.IMREAD_GRAYSCALE)

im = np.array(im)
h1 = np.full((3,3),1/9)
h2 = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
h3 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

filteredImage = signal.convolve2d(im, h1, mode='full')
cv2.imwrite("filtered_h1.png", filteredImage)