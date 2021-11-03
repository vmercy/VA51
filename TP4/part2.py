from math import exp, log
import cv2
import numpy as np
from math import log10, exp
from scipy import fftpack

def getSpectrum(im_fft):
  """Builds the Fourier spectrum of an image

  Args:
      im_fft (np.array): The source image matrix

  Returns:
      np.array: The spectrum image matrix
  """
  spectrum = np.zeros(im_fft.shape)
  for indexRow,row in enumerate(im_fft):
    for indexPixel, pixel in enumerate(row):
      spectrum[indexRow][indexPixel] = 10*log(abs(pixel),10)
  return spectrum

def buildGaussianMask(shape, sigma):
  img = np.zeros(shape)
  centerRow = shape[0]//2
  centerColumn = shape[1]//2
  for (indexRow, row) in enumerate(img):
    for (indexColumn, pixel) in enumerate(row):
      img[indexRow][indexColumn] = exp(-(pow(indexRow-centerRow,2)+pow(indexColumn-centerColumn,2))/(2*pow(sigma,2)))
  return img

def normalizeMask(mask):
  maxValue = np.max(mask)
  for (indexRow, row) in enumerate(mask):
    for (indexColumn, pixel) in enumerate(row):
      mask[indexRow][indexColumn] *= 255/maxValue
  return mask

if __name__ == "__main__":
  im = cv2.imread('ressources/road2.png',cv2.IMREAD_GRAYSCALE)
  gaussianMask = buildGaussianMask(np.shape(im),50)
  im_fft = np.fft.fft2(im)
  im_fft = np.fft.fftshift(im_fft)
  spectrum = getSpectrum(im_fft)
  filtered = im_fft*gaussianMask
  filteredSpectrum = spectrum*gaussianMask
  cv2.imwrite('fft.png',filteredSpectrum)
  inverted = np.fft.ifft2(filtered)
  inverted = np.abs(inverted)
  cv2.imwrite('gaussianFiltered.png',inverted)
