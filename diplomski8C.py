path='C:/Users/Y530/Downloads/rosalind_ba8c.txt'

import numpy as np
import math
from BA8A import euclidDist

def dpCenters(dp,centers):
  dist=list()
  for center in centers:
    dist.append(euclidDist(dp,center))
  mini=min(dist)
  return dist.index(mini)

def centersToClusters(data,centers):
  indC=list(dpCenters(dp,centers) for dp in data)
  return indC

def clusterToCenter(data,centers,i):
  assignedClusters=centersToClusters(data,centers)
  d=list()
  for dp,cluster in zip(data,assignedClusters):
    if i==cluster:
      d.append(dp)
  mean=np.round(np.mean(np.array(d), 0),3)
  return mean

def clustersToCenters(data,centers,k):
  newCenters=[clusterToCenter(data,centers,i) for i in range(k)]
  return newCenters

def lloyd(data,centers,k):
  flag=False
  while not flag:
    oldCenters=centers
    centers=clustersToCenters(data,centers,k)
    if np.array_equal(centers,oldCenters): flag=True
  return centers


if __name__=='__main__':
  with open(path,'r') as f:
    input=f.read().splitlines()
    
  k,m=input[0].split(' ')
  k=int(k)
  m=int(m)
  k,m=input[0].split(' ')
  k=int(k)
  m=int(m)
  data=input[1:]
  centers=input[1:1+k]
  
  for i in range(len(centers)):
    centers[i]=list(map(float, centers[i].split(' ')))

  for i in range(len(data)):
    data[i]=list(map(float,data[i].split(' ')))


  for el in lloyd(data,centers,k):
    print(*["%.3f" % (koord) for koord in el], sep=' ',file=open('output.txt','a'))