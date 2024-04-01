path='C:/Users/Y530/Downloads/rosalind_ba8b.txt'

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

def distortion(data,centers):
    sum=0
    for dp in data:
        sum+=(dpCenters(dp,centers)[0])**2
    res=(1/len(data))*sum
    return round(res,3)


if __name__=='__main__':
  with open(path,'r') as f:
    input=f.read().splitlines()
    
  k,m=input[0].split(' ')
  
  centers=input[1:1+int(k)]
  for i in range(len(centers)):
    centers[i]=centers[i].split(' ')
    centers[i]=list(np.float_(centers[i]))

  data=input[1+int(k)+1:]
  for i in range(len(data)):
    data[i]=data[i].split(' ')
    data[i]=list(np.float_(data[i]))
  
  res=distortion(data,centers)
  print(res)

