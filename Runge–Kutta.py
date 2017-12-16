import numpy as np
import matplotlib.pyplot as plt
def f(t,S):
    return -G*G*S*S/(D*D)+2*F*S+C*C

n=1000 #時間の分割
l=4
X=[0]*(n+1)
Y=[0]*(n+1)
S=[0]*(n+1)
Xhat=[0]*(n+1)
sum_loss=[0]*(n+1)
Var_loss=[0]*(n+1)
delta_t=1.0/n
double_loss=[0]*(n-1)
F=0.1
G=0.2
C=0.2
D=0.1
sigma=np.power(delta_t,0.5)
for k in range(l):
    m=10*np.power(10,k)
    moment=[[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        k1=f(i,S[i])
        k2=f(i+delta_t/2,S[i]+delta_t*k1/2)
        k3=f(i+delta_t/2,S[i]+delta_t*k2/2)
        k4=f(i+delta_t,S[i]+delta_t*k3)
        S[i+1]=S[i]+delta_t*(k1+2*k2+2*k3+k4)/6
    for j in range(m):
        X[0]=0
        Y[0]=0
        Xhat[0]=0
        for i in range(n):
            X[i+1]=X[i]+F*X[i]*delta_t+C*np.random.normal(0,sigma)
            Y[i+1]=Y[i]+G*X[i]*delta_t+D*np.random.normal(0,sigma)
            Xhat[i+1]=Xhat[i]+(F-(G*G*S[i]/(D*D)))*Xhat[i]*delta_t+(G*S[i]/(D*D))*(Y[i+1]-Y[i])
            moment[j][i]=np.absolute(X[i]-Xhat[i])
    for i in range(n-1):
        L1_loss=0
        loss=0
        for j in range(m):
            L1_loss=L1_loss+moment[j][i]/m
        for j in range(m):
            loss=loss+np.power(moment[j][i],2)
        Var_loss[i]=loss
        double_loss[i]=np.absolute(S[i]-Var_loss[i])
    plt.plot(double_loss)
plt.show()
