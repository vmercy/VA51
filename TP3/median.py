from scipy import signal
import cv2
import numpy as np

im = cv2.imread('ressources/I2filter.png', cv2.IMREAD_GRAYSCALE)

im = np.array(im)

filteredImage = signal.medfilt2d(im)
cv2.imwrite("median_filter.png", filteredImage)