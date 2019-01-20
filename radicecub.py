# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:27:55 2019

@author: Danilo
"""

tol=1e-10
maxiter=50
s=1234


def radicecub(tol,maxiter,s):
    niter=0
    if s<=0:
        niter=-1
        return ('errore')
    x0=s
    err=tol+1
    print('{:2}\t {:1.10f}\t {:+1.1e}'.format(niter,x0,err))
    while niter<maxiter and abs(err)>tol:
        rapp=s/(x0**2)
        x1=(1/3)*((2*x0)+rapp)
        err=(x1-x0)/x1
        x0=x1
        niter+=1
        print('{:2}\t {:1.10f}\t {:+1.1e}'.format(niter,x0,err))
    return(x0,niter) 