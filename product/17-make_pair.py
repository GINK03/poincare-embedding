import os

import sys

import glob

import json

import MeCab

terms = set( json.loads( open('terms.json').read() ) )

m = MeCab.Tagger('-Owakati')
for name in glob.glob('../../scraping-designs/rakuten-scrape/items/*'):
  obj = json.loads( open(name).read() )
  text = obj['item'] + obj['desc']
  _terms = set( m.parse( text ).strip().split() )
  fil = (terms & _terms)
  if len(fil) >= 2:
    print(fil)
