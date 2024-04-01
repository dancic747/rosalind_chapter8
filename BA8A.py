path='C:/Users/Y530/Downloads/rosalind_ba8a.txt'

import math
import numpy as np

def euclidDist(point1,point2):
  r=0
  for i in range(len(point1)):
    r+=(point1[i]-point2[i])**2
  return math.sqrt(r)

def dpCenters(dp,centers):
  dist=list()
  for center in centers:
    dist.append(euclidDist(dp,center))
  mini=min(dist)
  return mini, centers[dist.index(mini)]

def maxDistance(data,centers):
  d=dict()
  for dp in data:
    minDist,center=dpCenters(dp,centers)
    d[tuple(dp)]=minDist
  maxi=max(d.values())
  for key in d.keys():
    if d[key]==maxi:
      point=key
      break
  return point

def farthestFirstTraversal(k,data):
  centers=list()
  centers.append(tuple(data[0]))
  while len(centers)<k:
    point=maxDistance(data,centers)
    if point not in centers: centers.append(point)
  return centers     


if __name__=='__main__':
  with open(path,'r') as f:
    input=f.read().splitlines()
    
  k,m=input[0].split(' ')

  data=input[1:]
  for i in range(len(data)):
    data[i]=data[i].split(' ')
    data[i]=list(np.float_(data[i]))
  
  res=farthestFirstTraversal(int(k),data)
  for r in res:
    print(*r,sep=' ', file=open('output.txt','a'))
