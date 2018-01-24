# ポアンカレエンベッディング

Euclid空間にエンベッディングするようなword2vecは意味の上下関係が明示的に記されません。(情報としたあったとしても僅かでしょう)  

ポアンカレボールという双曲幾何学空間に埋め込むことで、効率的に意味の上位関係をとらえることができるとのことです[1]

## 理解
　ポアンカレボールはこのような、外周部に行くほど密になる球みたいなものなのです。
<div align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35317172-d165049e-0118-11e8-8704-33fb389696c9.png">
</div>
<div align="center"> 図1. ハニカム構造のPincare Ball(Wikipediaより)</div>
ポアンカレボールでは外に行くほど情報が密になり、空間が広がっているともとらえます。
 
 数式で表現するとこのようになって、
<div align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35318593-5bd1d714-011f-11e8-9d2e-5091d9851035.png">
</div>
gEというユークリッド距離がxが1に近づけば無限に大きくなることがわかります。

このポアンカレボール上にある二点間の距離はこのように表現され、単純なユークリッド距離ではないことが見て取れます。  
<div align="center">
  <img width="380px" src="https://user-images.githubusercontent.com/4949982/35318751-1c334ce0-0120-11e8-98d1-25c896338356.png">
</div>

この距離関数に基づいて損失関数L(Θ)を定義します。
<div align="center">
  <img width="380px" src="https://user-images.githubusercontent.com/4949982/35318870-a2a779b8-0120-11e8-880f-ff7a1d36ecc4.png">
</div>

双極幾何学空間に埋め込むと、情報が何らかの上下関係を持っており、木構造で表現できるとき、ルートノード（つまり抽象度が高い）方が真ん中にきて、枝葉に近いほど、外周部に行く傾向があるとのことで、これはポアンカレ空間に木の幹と枝を配置しようと試みるとき、幹が真ん中にきて枝が外周に来るとおさまりがいいのは、直感的に理解できると思います。  

なんか以前やったDeep Graph Convolutionに似ているなと思っていたら、Abejaさんのブログでも同様の記述を発見しました[2]

## 実験

### データセット

### 評価

### 参考文献
- [1] [Poincaré Embeddings for Learning Hierarchical Representations](https://arxiv.org/abs/1705.08039)
- [2] [異空間への埋め込み！Poincare Embeddingsが拓く表現学習の新展開](http://tech-blog.abeja.asia/entry/poincare-embeddings)
