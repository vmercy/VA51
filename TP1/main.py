from math import *
from textwrap import fill
import numpy as np
from PIL import Image, ImageDraw

def printMatrix(matrix):
  for line in matrix:
    print(line,'\n')

def createCMS(crs, cts):
  cms = np.concatenate((crs, np.transpose(np.array([cts]))),axis=1)
  return cms

def prp(cX):
  prp_x = cX[0]/cX[2]
  prp_y = cX[1]/cX[2]
  return np.array([prp_x,prp_y,1],dtype=float)

sP = [[-1,-1,0,1],[1,-1,0,1],[1,1,0,1],[-1,1,0,1]]

cts = [0,0,10,1]

alpha = pi
beta = pi/3
gamma = pi/12

alpha_u = 700
alpha_v = 700
u_0 = 400
v_0 = 300

K = [[alpha_u,0,u_0],[0,alpha_v,v_0],[0,0,1]]

crx = np.array([[1,0,0],[0,cos(alpha),-sin(alpha)],[0,sin(alpha),cos(alpha)]])
cry = np.array([[cos(beta),0,sin(beta)],[0,1,0],[-sin(beta),0,cos(beta)]])
crz = np.array([[cos(gamma),-sin(gamma),0],[sin(gamma),cos(gamma),0],[0,0,1]])

crs = np.matmul(crz,cry,crx)

crs = np.concatenate((crs, np.array([[0,0,0]])),axis=0)

cms = createCMS(crs,cts)

def getPixelCoordinates(sp):
  global K, cms
  return np.matmul(K, prp(np.matmul(cms, np.transpose(np.array([sp])))).T)

def getPixelPoints(sP):
  pointsToDraw = []
  for i in sP:
    pointsToDraw.append(getPixelCoordinates(i))
  return pointsToDraw

pointsToDraw = getPixelPoints(sP)

def drawPoints(points):
  diam = 10
  i = Image.new('RGB', (800,600), 'white')
  draw = ImageDraw.Draw(i)
  for point in points:
    draw.ellipse([(point[0]-diam, point[1]-diam), (point[0]+diam, point[1]+diam)], fill='red')
  i.save('image_camera_VA51_TP1.png')

drawPoints(pointsToDraw)
#printMatrix(getPixelCoordinates(sP[0]))

