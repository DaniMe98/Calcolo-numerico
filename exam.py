# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:18:58 2019

@author: Danilo
"""
import numpy as np
def f(x): return ((np.sin(x))/x)-x

x0=1
x1=.9
tol=1e-10
maxiter=50

def secanti(f,x0,x1,tol,maxiter):
    niter=0
    fx0=f(x0)
    fx1=f(x1)
    err=tol+1
    print('{:2}\t {:1.10f}\t {:+1.1e}'.format(niter,x1,err))
    while abs(err)>tol and niter<maxiter:
        molt=(fx1*x1)-(fx1*x0)
        div=fx1-fx0
        x2=x1-(molt/div)
        fx2=f(x2)
        x0=x1
        fx0=fx1
        x1=x2
        fx1=fx2
        err=(x1-x0)/x1
        niter+=1
        print('{:2}\t {:1.10f}'.format(niter,x1))
    return(x1,niter)    
    
  
def g(x): 
    valore=x**2
    return np.sqrt(1-valore)    

a=0
b=1    
n=4

def trapezi(g,a,b,n):
    h=(b-a)/n
    x0=a
    gx0=g(x0)
    som=0
    somma=0
    for j in range(1,int(n-1)):
        index=j*h
        ind=(j-1)*h
        val=a+index
        val1=a+ind
        som+=g(val)
        Ea=g(val)-g(val1)
    som*=2
    indice=n*h
    gxn=g(indice+a)
    somma=gx0+som+gxn
    In=(h/2)*somma
    return (In,abs(Ea))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    