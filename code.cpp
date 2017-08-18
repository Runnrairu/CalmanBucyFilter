#include <iostream>
#include <random>
#include<math.h>
using namespace std;

double Haar(int k,int n,double t);
double sdlab_normal(double mu, double sigma);
double sdlab_uniform();
int main(){
  double F,G,C,D;
  int n=5+1;
   F=0.5;
  G=0.6;
  C=0.3;
   D=0.2;
    double X[n],Y[n],W[n],B[n],Xhat[n];
    X[0]=0;
   Y[0]=0;
    Xhat[0]=0;
   int Im=pow(2,n)+1;
int i;
int j;
int l;

for(i=0;i<=10;i++){
    for(int j=1;j<=Im;j=j+2){
         double a;
         a=sdlab_normal(0,1);
         double b;
         b=sdlab_normal(0,1);
         for(int l;l<=n;l++){
         W[l]=W[l]+Haar(j,i,l)*a;
         B[l]=B[l]+Haar(j,i,l)*b;
         }  
    }
}
double deltat=1/n;
for(int l=1;l<=n;l++){
X[l+1]=X[l]+deltat*F*X[l]+C*(B[l+1]-B[l]);
Y[l+1]=Y[l]+deltat*G*X[l]+D*(W[l+1]-W[l]);
}
for(l=1;l<n;l++){
Xhat[l]=(F-(pow(G,2)*S[l]/pow(D,2)))*Xhat[l]*deltat+(G*S[l]/pow(D,2))*(Y[l+1]-Y[l]);
}
for(l=1;l<n;l++){
print X[l];
} 
for(l=1;l<n;l++){
print Xhat[l];
} 




    return 0;}
double Haar(int k,int n,double t){
if ((k-1)/pow(2,n)<=t && t<k/pow(2,n)){
        return (t-(k-1)/pow(2,n))*pow(2,(n-1)/2);
} else if(k/pow(2,n)<=t && t<(k+1)/pow(2,n)){
       return ((k+1)/pow(2,n)-t)*pow(2,(n-1)/2);
}else{return 0;}
}

double sdlab_uniform()
{
  double ret = ((double) rand() + 1.0) / ((double) RAND_MAX + 2.0);
  return ret;
}

double sdlab_normal(double mu, double sigma)
{
  double  z = sqrt(-2.0 * log(sdlab_uniform())) *
    sin(2.0 * M_PI * sdlab_uniform());
 
  return mu + sigma * z;
}
