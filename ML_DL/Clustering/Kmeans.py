#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:36:34 2021

@author: diegobarbosa
"""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

NUM_CLASSES=4
NUM_FEATURES=2

def euclidean(sample,center):
    return np.sqrt(distance.euclidean(sample,center))

def nearest_center(sample, centers):
    distances=[]
    for i in range(len(centers)):
        distances.append(euclidean(sample,centers[i]))
    return np.argmin(distances)

X,y= make_blobs(n_samples=200, n_features=NUM_FEATURES, centers=NUM_CLASSES, random_state=14)
fig,axs=plt.subplots(1,5,figsize=(18,3))

centers=np.random.randn(NUM_CLASSES,2)

for epoch,ax in zip(range(5),axs):
    ax.scatter(X[:,0],X[:,1], c='y', s=7)
    ax.scatter(centers[:,0],centers[:,1], marker='*', c='r',s=150)
    ax.set_title('epoch: '+format(epoch))
    sum_n_class=np.zeros((NUM_CLASSES,2))
    total_n_class=np.zeros((NUM_CLASSES,1))
    
    for i in range(len(X)):
        center=nearest_center(X[i],centers)
        total_n_class[center]+=1
        sum_n_class[center][0]+=X[i][0]
        sum_n_class[center][1]+=X[i][1]
        
    for center in range(NUM_CLASSES):
        if total_n_class[center]>0:
            centers[center][0]=sum_n_class[center][0]/total_n_class[center]
            centers[center][1]=sum_n_class[center][1]/total_n_class[center]
        else:
            centers[center]=np.random.rand(2)

plt.savefig('Kmeans.pdf')
plt.show()
