# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:20:14 2019

@author: Danilo
"""
import numpy as np


def elleu(A):
    (m,n)=A.shape
    L=np.eye(n)
    for k in range(0,n-1):
        if A[k,k]==0:
            print('pivot nullo')
            return [],[]
        for i in range(k+1,n):
            L[i,k]=A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j]=A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    return(L,U)        
    
def elleupp(A):
    (m,n)=A.shape
    p=np.zeros(n,dtype=int)
    L=np.eye(n)
    for k in range(0,n-1):
        r=np.abs(A[k:n,k]).argmax()
        r=r+k
        p[k]=r
        A[[k,r],:]=A[[r,k],:]
        if A[k,k]==0:
            print('pivot nullo')
            return [],[]
        for i in range(k+1,n):
            L[i,k]=A[i,k]/A[k,k]
            for j in range(0,n-1):
                A[i,j]=A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    P=np.eye(n)
    for k in range(0,n-1):
        P[[k,p[k]],:]=P[[p[k],k],:]
    return L,U,P,p    
        
A=np.matrix([[-2,-4,-4],[2,-1,0],[4,-2,-4]])
(L,U)=elleu(A.copy())
print(np.dot(L,U)) 
print(L)
print(U)   

A=np.matrix([[-2,-4,-4],[2,-1,0],[4,-2,-4]])
(L,U,p,P)=elleupp(A.copy())
print(np.dot(L,U)-np.dot(P,A))
print(L)
print(U)




    
    
    