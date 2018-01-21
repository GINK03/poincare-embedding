import gzip

import pickle

import numpy as np

import json

term_vec = pickle.loads(gzip.decompress(open('term_vec.pkl.gz', 'rb').read()))

source = term_vec['iphone']
#print(source)

term_rel = {}

for term, target in term_vec.items():
  d = (source*target).sum()
  b = np.linalg.norm(target)*np.linalg.norm(source)
  term_rel[ term ] = d/b

terms = []
for term, rel in sorted(term_rel.items(), key=lambda x:x[1]*-1)[0:250]:
  # print(term, rel)
  if 'iphone' not in term:
    terms.append( term )

open('terms.json', 'w').write( json.dumps(terms, indent=2, ensure_ascii=False) )
