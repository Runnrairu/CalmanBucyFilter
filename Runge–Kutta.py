import math
import random
def f(t,S):
	return -G*G*S*S/(D*D)+2*F*S+C*C
	
n=1000
X=[0]*(n+2)
Y=[0]*(n+2)
S=[0]*(n+2)
Xhat=[0]*(n+2)
delta_t=1000/n
F=0.1
G=0.2
C=2.0
D=3.0
S[0]=1
Xhat[0]=1
for i in range(n):
	k1=f(i,S[i])
	k2=f(i+delta_t/2,S[i]+delta_t*k1/2)
	k3=f(i+delta_t/2,S[i]+delta_t*k2/2)
	k4=f(i+delta_t,S[i]+delta_t*k3)
	S[i+1]=S[i]+delta_t/6*(k1+2*k2+2*k3+k4)

for i in range(n):
	X[i+1]=F*X[i]*delta_t+C*random.gauss(0,delta_t)
	Y[i+1]=G*X[i]*delta_t+D*random.gauss(0,delta_t)
for i in range(n):
	Xhat[i+1]=(F-(G*G*S[i]/(D*D)))*Xhat[i]*delta_t+G*S[i]/(D*D)*(Y[i+1]-Y[i])

print X
print "ここからS"
print Xhat
print S
