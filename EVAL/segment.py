import cv2
import numpy as np
from numpy.lib.function_base import select
from numpy.lib.type_check import imag

def mean():
  pass

""" def getBorderPoints(outputImage, borderPoints):
  newBorderPoints = []
  for point in borderPoints:
    if(point[0]!=0 and point[0]!=)
    newBorderPoints.append((point[0]-1,point[1]),) """

def segmentation(image, startingPoint, treshold):
  selectedPoints = [] #Liste des points sélectionnés (appartenant à la zone segmentée)
  borderPoints = [startingPoint] #Liste des points bordants la region
  outputImage = np.zeros(image.shape)
  outputImage[startingPoint] = 1
  currentMean = 0
  currentPoint = startingPoint #coordonnnées du point courant (ayant la plus petite difference)
  while currentMean<treshold:
    for borderPoint in borderPoints:
      i = borderPoint[0]
      if i == 0 : i=1
      else if i==
      j = borderPoint[1]
      voisins = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for voisin in voisins:
           if outputImage[voisin]!=1.0: #si le voisin n'appartient pas déjà à la région
              borderPoints.append()
    """ for i, row in enumerate(image[1:image.shape[1]-1,1:image.shape[0]-1]):
      for j, pixelValue in enumerate(row): """




if __name__ == "__main__":
  im1 = cv2.imread('ressources/route1.png', cv2.IMREAD_GRAYSCALE)
  im1 = np.array(im1)
  im1 = im1/255.0
  segmentation(im1, (250,226),0.2)
  print(im1[3:3])