import os

import sys

import glob

import json

import MeCab

import itertools
terms = set( json.loads( open('terms.json').read() ) )

m = MeCab.Tagger('-Owakati')
pairs = []
for name in glob.glob('../../scraping-designs/rakuten-scrape/items/*'):
  obj = json.loads( open(name).read() )
  text = obj['item'] + obj['desc']
  _terms = set( m.parse( text ).strip().split() )
  fil = (terms & _terms)
  if len(fil) >= 2:
    print(fil)
    for pair in itertools.combinations(fil, 2):
      pairs.append( pair )

open('pairs.json', 'w').write( json.dumps(pairs, indent=2, ensure_ascii=False) )
