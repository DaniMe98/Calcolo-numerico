# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:51:17 2019

@author: Danilo
"""
import numpy as np

def f(x): return np.sin(x)

a=0
b=np.pi
n=4

def simpson(f,a,b,n):
    som=0
    som1=0
    h=(b-a)/n
    x0=a
    fx0=f(x0)
    for j in range(1,int((n/2)+1)):
        index=2*j
        val=a+(index*h)
        som+=f(val)
    som*=2
    for i in range(1,int((n/2))):
        indice=(2*i)-1
        val1=a+(indice*h)
        som1+=val1
    som1*=4
    somme=som+som1+fx0
    ultimo=a+(n*h)
    fxn=f(ultimo)
    iN=(h/3)*(somme+fxn)
    return('{:1.10f}'.format(iN))    
    