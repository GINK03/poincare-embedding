import os

import glob

import MeCab

import itertools

import dbm

import hashlib

import pickle, gzip

db = dbm.open('db.db', 'c')
m = MeCab.Tagger('-Ochasen')
for name in glob.glob('../../scraping-designs/rakuten-scrape/items/*'):
  terms = m.parse(open(name).read()).strip().split('\n')
  terms = [term.split('\t')[0] for term in terms if '名詞' in term]
  terms = set(terms)
  for pair in itertools.combinations(terms,2):
    val = gzip.compress( pickle.dumps(pair) )
    key = hashlib.sha256( val ).hexdigest()
    db[key] = val
