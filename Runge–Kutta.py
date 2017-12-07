# -*- coding: utf-8 -*-
import math
import numpy as np
import random
def f(t,S):
    t=float(t/n)
    return -G*G*S*S/(D*D)+2*F*S+C*C
 
n=1000 #時間の分割
m=1000 #サンプルパスの数
X=[0]*(n+1)
Y=[0]*(n+1)
S=[0]*(n+1)
Xhat=[0]*(n+1)
sum_loss=[0]*(n+1)
moment=[[0 for i in range(n)] for j in range(m)]
Var_loss=[0]*(n+1)
delta_t=1.0/n
double_loss=[0]*(n+1)
F=1.0
G=2.0
C=2.0
D=10.0
sigma=np.power(delta_t,0.5)
S_delta=1.0/n
for i in range(n):
	k1=f(i,S[i])
	k2=f(i+S_delta/2,S[i]+S_delta*k1/2)
	k3=f(i+S_delta/2,S[i]+S_delta*k2/2)
	k4=f(i+S_delta,S[i]+S_delta*k3)
	S[i+1]=S[i]+S_delta*(k1+2*k2+2*k3+k4)/6
for j in range(m):
    for i in range(n):
        X[i+1]=F*X[i]*delta_t+C*np.random.normal(0,delta_t)
        Y[i+1]=G*X[i]*delta_t+D*np.random.normal(0,delta_t)
        Xhat[i+1]=(F-(G*G*S[i]/(D*D)))*Xhat[i]*delta_t+G*S[i]/(D*D)*(Y[i+1]-Y[i])
        moment[j][i]=X[i]-Xhat[i]

for i in range(n):
    loss=0
    for j in range(m):
        loss=loss+np.power(moment[j][i],2)
    Var_loss[i]=loss/m
    double_loss[i]=np.absolute(S[i]-Var_loss[i])
print(double_loss)
