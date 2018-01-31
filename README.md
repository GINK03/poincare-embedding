# ポアンカレエンベッディング

Euclid空間にエンベッディングするようなword2vecは意味の上下関係が明示的に記されません。(情報としたあったとしても僅かでしょう)  

ポアンカレボールという双曲幾何学空間に埋め込むことで、効率的に意味(や木構造)の上位関係をとらえることができます[1]

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
これをSGDやFBリサーチの論文ではRiemannianSGDというオプティマイザを利用して最適化しています  

双極幾何学空間に埋め込むと、情報が何らかの上下関係を持っており、木構造で表現できるとき、ルートノード（つまり抽象度が高い）方が真ん中にきて、枝葉に近いほど、外周部に行く傾向があるとのことで、これはポアンカレ空間に木の幹と枝を配置しようと試みるとき、幹が真ん中にきて枝が外周に来るとおさまりがいいのは、直感的に理解できると思います。  

なんか以前やったDeep Graph Convolutionに似ているなと思っていたら、Abejaさんのブログでも同様の記述を発見しました[2]　　

何でもいいので、優秀なエンベッティングは距離空間を適宜定義することでその空間の形に応じた特性を獲得できそうということでもあり、ポアンカレボールは意味的、木構造的な関係を獲得できるし、別の距離空間ではそのようなものが定義できるのだと思います。  


## 実験
pythonの言語処理ライブラリであるgensimですでにpoincare embeddingが実装されています。  

可視化の方法もjupyterを用いて簡単にできるので、なんかの情報のペアで木構造を持つと仮定できるデータセットがあれば、学習することができます。

poincare embeddingの論文では、動物名と動物の所属する種類などのペアのデータセットを利用して、poincareに埋め込んで評価しています。 
```console
(ライオン, ネコ科)
(ネコ科, 哺乳類)
...
```
こんなどちらが上位の概念化は順序がむちゃくちゃでいいので、ペアのデータセットがたくさん作成します

### データセット
旧日本海軍の艦種のいくつかのデータセットを用いてやってみましょう。

軍艦を発信点にして、大分する艦種と、艦種と艦名のペアです。
```console
軍艦    駆逐艦
軍艦    戦艦
軍艦    巡洋艦
軍艦    空母
駆逐艦  陽炎型
駆逐艦  朝潮型
駆逐艦  吹雪型
駆逐艦  白露型
朝潮型  朝潮
朝潮型  大潮
朝潮型  満潮
...
```

### 可視化
gensimでの実装は、jupyterとplotlyを用いてこのようにすることで、簡単に可視化できます  
(おそらくFacebook ResearchのPyTorchでの実装は同じ方法は通用しませんが、こっちの方が本来性能はよさそうです)  
```python
import plotly
import gensim.viz.poincare

import pickle
model = pickle.loads(open('model.pkl','rb').read())
relations = pickle.loads(open('relations.pkl', 'rb').read() )

plotly.offline.init_notebook_mode(connected=False)
prefecutre_map = gensim.viz.poincare.poincare_2d_visualization(model=model,
                                                               tree=relations,
                                                               figure_title="艦種",
                                                               show_node_labels=model.kv.vocab.keys())
plotly.offline.iplot(prefecutre_map)
```

### 評価
ポアンカレボール上に配置するときに、乱択アルゴリズムでサンプリングするらしいので、小さいデータセットではきれいな円状に配置されませんが、おおむねそれらしい結果が得られています。（割り切ってランダムネスの影響を許容するといいでしょう）
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/35321964-eddf729a-012b-11e8-91e8-2679f32a1d10.png">
</div>
朝潮型が変なところに来ています。Optimizerの動作のラムダムネスにより変なところにきているようです 

なかなかgemsinで実行するとうまくいきませんね。（最適化アルゴリズムにSGDなどの乱択がはいるので仕方がないですが。。。）  

より、細やかに丁寧に距離函数を再定義できそうな実装系としてFacebook社のPytorchのSGDオプティマイザと距離函数を双曲線距離に定義した物を使うと、learning rateを最初に大きく取って少なくしていくなどの戦略が取れるので、より細やかに綺麗に学習が収束しそうです[3]  

<div align="center">
  <img width="450px" src="https://github.com/facebookresearch/poincare-embeddings/blob/master/wn-nouns.jpg">
</div>
<div align="center"> 図 Facebook ResearchによるPoincare Embedding</div>

### 参考文献
- [1] [Poincaré Embeddings for Learning Hierarchical Representations](https://arxiv.org/abs/1705.08039)
- [2] [異空間への埋め込み！Poincare Embeddingsが拓く表現学習の新展開](http://tech-blog.abeja.asia/entry/poincare-embeddings)
- [3] [facebookresearch/poincare-embeddings](https://github.com/facebookresearch/poincare-embeddings)
