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
for term, rel in sorted(term_rel.items(), key=lambda x:x[1]*-1)[0:150]:
  # print(term, rel)
  if 'ipad' not in term and '6s' not in term and 'plus' not in term and 'iphon' not in term and '5s' not in term and 'あいふぉん' not in term and 'アイフォン' not in term and 'アイフォーン' not in term and 'アイホン' not in term  and 'アイホーン' not in term:
    terms.append( term )

open('terms.json', 'w').write( json.dumps(terms, indent=2, ensure_ascii=False) )
