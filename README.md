# カルマンブーシーフィルタの実装
## カルマンブーシーフィルタとは
連続時間版のカルマンフィルタ。主に確率微分方程式に関する統計理論として研究されている。   
今回は次のような確率微分方程式を考える。  
  
<img src="https://latex.codecogs.com/gif.latex?dX_t=FX_t&space;dt&plus;C&space;dW_t" />
<img src="https://latex.codecogs.com/gif.latex?dY_t=GX_t&space;dt&plus;D&space;dW^*_t" />
  
ここで、観測できるのはYだけであるとする。この情報から、平均二乗誤差が最小になるようなXの推定量を構成したい。
今回は証明は省くが、平均二乗誤差が最小になる推定量は次のようにかける。  
　  
<img src="https://latex.codecogs.com/gif.latex?d\hat{X}_t=(F-\frac{G^2S_t}{D^2})\hat{X}_tdt+\frac{GS_t}{D^2}dY_t" />
    
ただし、Sは次の常微分方程式に従う、時刻tでの平均二乗誤差である。  
　　　  
<img src="https://latex.codecogs.com/gif.latex?S'_t=-\frac{G^2S^2_t}{D^2}+2FS+C^2" />
　  
このレポジトリでは、乱数によって生成されるサンプルパスを増やしていけば平均二乗誤差がSに収束することを数値的に確かめた。  
すなわち  
　    
<img src="https://latex.codecogs.com/gif.latex?E[|X_t-\hat{X}_t|^2]=S_t" />
　    
が成り立つことを、数値実験により確認した。  
### 参考文献
[1]Bernt Oksendal,Stochastic Differential Equations: An Introduction with Applications(2010)  
[2]小川重義,確率微分方程式の数値解法(2001)

