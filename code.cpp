#include <iostream>
#include <random>
#include<math.h>
using namespace std;

double Haar(int k,int n,double t);
double sdlab_normal(double mu, double sigma);
double sdlab_uniform();
int main(){
  double F,G,C,D;
  int n=1000;
   F=0.5;
  G=0.6;
  C=0.3;
   D=0.2;
    double X[n],Y[n],W[n],B[n];
　X[0]=0;
   Y[0]=0;

for(int i=0;i<=10000;i++){
    for(int j=0;j<=n;j++){

    
    }
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
