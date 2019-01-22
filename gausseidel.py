# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:51:45 2019

@author: Danilo
"""

import numpy as np
import scipy.linalg as sl

tol=1e-5
maxiter=15

def gaussseidel(A,b,x0,tol,maxiter):
    niter=0
    err=1+tol
    
    L=np.tril(A) #creazione matrice triangolare inferiore
    U=np.triu(A,1) #creazione matrice triangolare superiore
    
    resul=x0
    n1x0=np.linalg.norm(x0,1)
    n1resul=np.linalg.norm(resul,1)
    
    while err>tol and niter<maxiter:
        x0=resul
        n1x0=np.linalg.norm(x0,)
        resul=sl.solve_triangular(L,b-np.dot(U,x0),lower=True)
        n1resul=np.linalg.norm(resul,1)
        niter+=1
        err=abs(n1x0-n1resul)/abs(n1resul)
    return (resul,niter)    

A=np.array([[2.4,-0.8,-0.7],[0.5,1.5,0.7],[-0.1,0.8,2.1]])
b=np.array([0.9,2.7,2.8])
x0=np.array([2,2,2])

print(gaussseidel(A,b,x0,tol,maxiter))