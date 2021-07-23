#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 19:26:16 2021

@author: diegobarbosa
"""


import random
import matplotlib.pyplot as plt


X=list(range(40))
y=[]
for i in range(len(X)):
    y.append(20+X[i]+random.random()*20)
    
fig,axs=plt.subplots(1,4,figsize=(15,4))

def sort(unsorted_list):
    return (sorted(unsorted_list,key=lambda x: x[2])) #sort by distance

def plot(fig, X, y, parameters, label):
    axs[fig].plot(X,y, parameters, label=label)
    axs[fig].legend(); axs[fig].grid();
    return 

def KNN_p(k,X1,y1,x,figure):
    
    distance=[]
    
    for i in range(len(X)):
        distance.append((X1[i],y1[i],(x-X1[i])**2))
        
    sorted_list=sort(distance)
    x_neig, y_neigh= [],[]
    y_pred=0.0
    
    for i in range(k):
        y_pred+=sorted_list[i][1]
        x_neig.append(sorted_list[i][0])
        y_neigh.append(sorted_list[i][1])
    y_pred/=k
    
    plot(figure,X1,y1,'y.',"samples")
    plot(figure,x_neig,y_neigh,'k.','neighbourhood')
    plot(figure,x,y_pred,"r+",'Prediction')
    axs[figure].set_xlabel('{:1.0f}'.format(k)+ 'neighbors')
    return y_pred

KNN_p(2,X,y,7.6,0)
KNN_p(4,X,y,20.5,1)
KNN_p(7,X,y,36.2,2)
KNN_p(15,X,y,24.3,3)
plt.savefig("KNN.pdf")
plt.show()
