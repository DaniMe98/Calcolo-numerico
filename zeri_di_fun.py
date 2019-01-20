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
   
    fb= f(b)
    fa=f(a)
    niter = 0
    rapp=(b-a)/(fb-fa)
    y=a-(fa*rapp)
    fy=f(y)
    res =[]
    res.append(fy)
    err=abs(y-a)
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,y,err))
    
    while niter < nmax and err> tol:
        a=y
        fa=fy
        niter+=1
        y=a-fa*rapp 
        fy= f(y)
        err=rapp
        res.append(fy)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,y,err))
    return (y,niter,res)

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

def corde(f,x,pend,tol,nmax):
    niter=0
    fx=f(x)
    err=tol+1
    res=[]
    res.append(fx)
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x,err))
    while niter<nmax and err>tol:
        rapp=-(fx/pend)
        y=x+rapp
        fy=f(y)
        err=x-y
        niter+=1
        x=abs(y)
        fx=fy
        res.append(fx)
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter,x,err))
    return(x,niter,res)    
        
def secanti(f,x,tol,nmax):
    
    fx=f(x)
    x1=x+.2
    fx1=f(x1)
    niter=0
    err=tol+1
    res=[]
    res.append(fx1)
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x1,err))
    while niter<nmax and abs(err)>tol:
        rapp=(fx1-fx)/(x1-x)
        x2=x1-(fx1/rapp)
        fx2=f(x2)
        x=x1
        fx=fx1
        x1=x2
        fx1=fx2
        err=x1-x
        niter+=1
        res.append(fx1)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x1,err))
    return(x1,niter,res)    
    
def quasinewton(f,x,tol,nmax):
    niter=0
    fx=f(x)
    err=tol+1
    h=.25
    res=[]
    res.append(fx)
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,err))
    while err>tol and niter<nmax:
        c=x+h
        fxh=f(c)
        rapp=(fxh-fx)/h
        x1=x-(fx/rapp)
        fx1=f(x1)
        x=x1
        fx=fx1
        err=x+x1
        niter+=1
        res.append(fx)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,err))
    return(x,niter,res)    
    
    

x=.7
tol=1e-16
nmax=53 #numero massimo iterate
pend=1.92 #pendenza della retta secante passante da x e a

out_bis=bisezioni(f,0,1,tol,nmax)
out_fal=regulafalsi(f,0,1,tol,nmax)
out_newt=newton(f,df,x,tol,nmax)    #richiama il metodo newton
out_corde=corde(f,5,pend,tol,nmax)    #richiama il metodo delle corde
out_sec=secanti(f,x,tol,nmax)
out_qn=quasinewton(f,x,tol,nmax)
   
x_bis=np.arange(0,out_bis[1]+1)
y_bis=np.array(out_bis[2])
y_bis=np.abs(y_bis)
plt.semilogy(x_bis,y_bis)#richiama il metodo succ.bisezioni

x_newt=np.arange(0,out_newt[1]+1)
y_newt=np.array(out_newt[2])
y_bis=np.abs(y_bis)
plt.semilogy(x_newt,y_newt)



x_fal=np.arange(0,out_fal[1]+1)
y_fal=np.array(out_fal[2])
y_fal=np.abs(y_fal)
plt.semilogy(x_fal,y_fal)

x_cor=np.arange(0,out_corde[1]+1)
y_cor=np.array(out_corde[2])
y_cor=np.abs(y_cor)
plt.semilogy(x_cor,y_cor)

x_sec=np.arange(0,out_sec[1]+1)
y_sec=np.array(out_sec[2])
y_sec=np.abs(y_sec)
plt.semilogy(x_sec,y_sec)

x_qn=np.arange(0,out_qn[1]+1)
y_qn=np.array(out_qn[2])
y_qn=abs(y_qn)
plt.semilogy(x_qn,y_qn)




