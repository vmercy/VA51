from math import log
import cv2
import numpy as np
from math import log10
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

def centralSquareMask(img, size):
  """Add a square mask in the center of an image

  Args:
      img (np.array): The source image matrix
      size (int): The side length of central square in px

  Returns:
      np.array: The masked image matrix
  """
  leftStart = (np.shape(img)[1]-size)//2
  upperStart = (np.shape(img)[0]-size)//2
  img[upperStart:upperStart+size,leftStart:leftStart+size] = 0
  return img

def maskAllButSquareCenter(img, size):
  """Masks all image except a square in the center

  Args:
      img (np.array): The source image matrix
      size (int): The side length of central square in px

  Returns:
      np.array: The masked image matrix
  """
  leftStart = (np.shape(img)[1]-size)//2
  upperStart = (np.shape(img)[0]-size)//2
  newImg = np.zeros(np.shape(img))
  newImg[upperStart:upperStart+size,leftStart:leftStart+size] = img[upperStart:upperStart+size,leftStart:leftStart+size]
  return newImg

if __name__ == "__main__":
  im = cv2.imread('ressources/road1.png',cv2.IMREAD_GRAYSCALE)
  im_fft = np.fft.fft2(im)
  im_fft = np.fft.fftshift(im_fft)
  spectrum = getSpectrum(im_fft)
  filtered = maskAllButSquareCenter(im_fft,50)
  filteredSpectrum = maskAllButSquareCenter(spectrum,50)
  cv2.imwrite('fft.png',filteredSpectrum)
  inverted = np.fft.ifft2(filtered)
  inverted = np.abs(inverted)
  print(inverted)
  cv2.imwrite('filteredCenterSquareOnly.png',inverted)
