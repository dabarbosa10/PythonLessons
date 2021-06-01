import matplotlib.pyplot as plt
import random
import numpy as np

def gradient(X,y,alpha,b,w):
    dw=0.0
    db=0.0
    for i in range(len(X)):
        aux=-2.0*(y[i]-(w*X[i]+b))
        db=db+aux
        dw=dw+X[i]*aux
    aux=1.0/float(len(X))
    b=b-aux*db*alpha
    w=w-aux*dw*alpha
    return b,w

def gradient2(X,y,alpha,b,w):
    aux=-2.0*(y-(w*X+b)).sum()
    b=b-alpha*aux/float(len(X))
    w=w-alpha*aux/float(len(X))
    return b,w

def plot(fig,X,y,b,w,epochs):
    axs[fig].plot(X,y,'yo',label='Samples')
    X=np.array(X)
    axs[fig].plot(X, w*X+b, 'k-', label='Regression loss: '+' {:9.2f}'.format(loss(X,y,b,w)))
    axs[fig].set_xlabel('{:5.0f}'.format(epochs)+' epochs')
    axs[fig].legend(); axs[fig].grid();
    return

def model(X,y,alpha,b,w,epochs):
    fig=0
    for e in range(epochs):
        b,w= gradient2(X,y,alpha,b,w)
        if e%3000==0:
            plot(fig,X,y,b,w,e)
            fig+=1
    return b,w

def prediction(x,b,w):
    return(x*w+b)

def loss(X,y,b,w):
    sum1=0
    for i in range(len(X)):
        sum1+=(y[i]-prediction(X[i],b,w))**2
    return sum1/len(X)

def create(n):
    X=np.array(list(range(40)))
    y=20+X+np.random.rand(40)*20
    return X,y
	