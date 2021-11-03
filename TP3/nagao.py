import cv2
import numpy as np

def rotateMatrix90DegreesCW(matrix):
  """Rotates a matrix by 90 degrees clockwise

  Args:
      matrix (list): matrix to rotate

  Returns:
      list: rotated matrix
  """
  return list(zip(*matrix[::-1]))

def buildNagaoWindows():
  """Builds nagao windows used as filters

  Returns:
      array: Array of np.array containing the nine nagao windows as matrix
  """
  upper = [[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
  corner = [[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
  center = [[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
  windows = [center]
  for i in range(4):
    upper = rotateMatrix90DegreesCW(upper)
    corner = rotateMatrix90DegreesCW(corner)
    windows.append(np.array(upper))
    windows.append(np.array(corner))
  return windows

def writeNagaoWindows(nagaoWindows):
  for index, window in enumerate(nagaoWindows):
    cv2.imwrite("nagaoWindows/%s.png"%index, 255*np.array(window))

def Variance(matrix):
  return np.var(matrix)

if __name__ == "__main__":
  nagaoWindows = buildNagaoWindows()
  im = cv2.imread('ressources/I2filter.png', cv2.IMREAD_GRAYSCALE)
  im = np.array(im)
  (imgHeight, imgWidth) = np.shape(im)
  newIm = np.zeros((imgHeight, imgWidth))
  inc = 0
  totalPixels = imgHeight*imgWidth
  for row in range(2,imgHeight-2):
    for column in range(2,imgWidth-2):
      pixelSurrounding = im[row-2:row+3,column-2:column+3]
      variances = []
      for window in nagaoWindows:
        pixelMul = np.multiply(pixelSurrounding, window)
        variances.append(Variance(pixelMul))
      minVar = np.min(np.array(variances))
      bestWindow = variances.index(minVar)
      newPixelValue = np.mean(pixelMul)
      newIm[row,column] = newPixelValue
      inc+=1
      print('Processing pixel %i of %i : %4.2f %%'%(inc,totalPixels,100*inc/totalPixels))
  cv2.imwrite('nagaoFiltered.png',newIm)