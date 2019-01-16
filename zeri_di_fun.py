# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:54:38 2019

@author: Danilo
"""
import numpy as np
import matplotlib.pyplot as plt

def df(x):    return 1+np.sin(x)

def f(x):    return x-np.cos(x)
    
def bisezioni(f,a,b,tol,nmax):
    x=0.5*(a+b)
    fa=f(a)
    fx=f(x)
    niter=0
    res=[]
    res.append(fx)
    print('{:2}\t {:1.15}\t {:+1.1e}'.format(niter,x,fx))
    while niter < nmax and .5*(b-a) > tol:  
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        fx=f(x)
        niter += 1
        res.append(fx)
        print('{:2}\t {:1.15}\t {:+1.1e}'.format(niter,x,fx))
    if .5*(b-a) > tol:
        niter = -1 
    return (x,niter,res)

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

def newton(f,df,x,tol,nmax):
    niter=0;
    err=tol+1
    res=[]
    res.append(f(x))
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x,err))
    while err>tol and niter<nmax:
        dfx=df(x)
        if dfx==0:
            niter=-1
            return(x,niter)
        fx=f(x)
        dx=-fx/dfx
        y=dx+x
        err=abs(dx)
        niter+=1
        res.append(f(y))
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,y,err))
        x=y
    return (y,niter,res) 

x=.7
tol=1e-15
nmax=100

out_bis=bisezioni(f,0,1,tol,nmax)
out_newt=newton(f,df,x,tol,nmax)

x_bis=np.arange(0,out_bis[1]+1)
y_bis=np.array(out_bis[2])
y_bis=np.abs(y_bis)
plt.semilogy(x_bis,y_bis)

x_newt=np.arange(0,out_newt[1]+1)
y_newt=np.array(out_newt[2])
y_bis=np.abs(y_bis)
plt.semilogy(x_newt,y_newt)













