# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:54:38 2019

@author: Danilo
"""
import numpy as np
def f(x):
    f=np.sin(x) 
    return f
    
def bisezioni(f,a,b,tol,nmax):
    x=0.5*(a+b)
    fa=f(a)
    fx=f(x)
    niter=0
    while niter < nmax and .5*(b-a) > tol:  
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        fx=f(x)
        niter += 1
    if .5*(b-a) > tol:
        niter = -1 
    return (x,niter,fx)

def regulafalsi(f,a,b,tol,nmax):
    x= b-(f(a)*(b-a)/(f(b)-f(a)))
    fx= f(x)
    fa=f(a)
    niter = 0
    res =[]
    res.append(fx)
    
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    
    while niter < nmax and b-(f(a)*(b-a)/(f(b)-f(a))) > tol:
        if fx*fa<0:
            b=x
        else:
            a=x
            fa=fx
        niter+=1
        x= b-(f(a)*(b-a)/(f(b)-f(a)))
        fx= f(x)
        res.append(fx)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    return (x,niter,res)