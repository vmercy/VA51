import cv2
import numpy as np
from numpy.lib.type_check import imag

inputImageFilename = 'otsu4'
image = cv2.imread('ressources/otsu/%s.png' % inputImageFilename, cv2.IMREAD_GRAYSCALE)
image = np.array(image)

histoHeight = np.size(image, 0)
nbPixels = np.size(image,0)*np.size(image,1)
histo = []
probas = []

def h(n):
  """Computes histogram value for a grayscale intensity level

  Args:
      n (int): The grayscale intensity level

  Returns:
      int: The number of pixels having n as intensity level
  """
  global image
  count = np.count_nonzero(image == n)
  return count

def p(n):
  """Computes probability value for a grayscale intensity level

  Args:
      n (int): The grayscale intensity level

  Returns:
      float: The probability associated to n
  """
  global image, nbPixels
  return float(h(n)/nbPixels)

def math_sum(start, end, callable):
  """Computes the mathematical sum

  Args:
      start (int): Starting index (included)
      end (int): Ending index (included)
      callable (string): Function to call on each element

  Returns:
      float: The sum where each term is computed with callable
  """
  sum = 0
  for i in range(start, end+1):
    sum+=eval(callable+'(i)')
  return sum

def wb(T):
  return math_sum(0,T,'p')+0.0001 #FIXME: division by zero error with otsu4

def nxpn(T):
  return T*p(T)

def ub(T):
  return 1/wb(T)*math_sum(0,T,'nxpn')

def ob2_insideSum(T):
  return (pow(T-ub(T)),2)*p(T)

def ob2(T):
  return 1/wb(T)*math_sum(0,T,'ob2_insideSum')

def wf(T):
  return 1-wb(T)

def uf(T):
  return 1/wf(T)*math_sum(T+1,255,'nxpn')

def of2_insideSum(T):
  return (pow(T-uf(T),2))*p(T)

def of2(T):
  return 1/wf(T)*math_sum(T+1,255,'of2_insideSum')

def ow2(T):
  return wb(T)*ob2(T)+wf(T)*of2(T)

def ob2(T):
  return wb(T)*wf(T)*pow(ub(T)-uf(T),2)

for i in range(0,255):
  histo.append(h(i))
  probas.append(p(i))

Topt = -1
ob2Max = 0

for tresHold in range(255):
  interClassVariance = ob2(tresHold)
  if(interClassVariance>ob2Max):
    ob2Max = interClassVariance
    Topt = tresHold

print(Topt)

""" histoMax = np.max(histo)

for index, pixelValue in enumerate(histo):
  cv2.line(result, (index,histoHeight-2), (index,histoHeight-int(pixelValue*histoHeight/nbPixels)), (0,0,0), 1)
  result[histoHeight-1][index]=index
  result[histoHeight-2][index]=0

cv2.imwrite('otsu_results/%s.png',result) %inputImageFilename """