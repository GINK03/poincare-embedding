import pickle

import plotly
import gensim.viz.poincare


model = pickle.loads(open('model.pkl','rb').read())
relations = pickle.loads(open('relations.pkl', 'rb').read() )

for key in model.kv.vocab.keys():
  print(key)
  print(model.kv[key])
