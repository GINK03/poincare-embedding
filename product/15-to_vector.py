import os

import numpy as np

import pickle

import gzip
term_vec = {}
for line in open('model.vec'):
  line = line.strip()
  ents = line.split(' ')
  term = ents.pop(0)
  vec = [float(v) for v in ents]
  print(term)
  vec = np.array(vec)
  if vec.shape == (100,):
    term_vec[term] = np.array(vec)

open('term_vec.pkl.gz', 'wb').write( gzip.compress(pickle.dumps(term_vec)) )
