import cv2

im1 = cv2.imread('ressources/Ibefore.png', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('ressources/Iafter.png', cv2.IMREAD_GRAYSCALE)

diff = abs(im1-im2)

cv2.imwrite('result.png', diff)
