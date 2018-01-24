import os

import glob

import MeCab

import itertools

import dbm

import hashlib

import pickle, gzip

import re

import json
m = MeCab.Tagger('-Owakati')

files = glob.glob('../../scraping-designs/rakuten-scrape/items/*')
size = len(files)
buff = ''
for index, name in enumerate(files):
  print(index, '/', size)
  obj = json.loads( open(name).read().lower() )

  text = obj['item'] + obj['desc']
  buff += m.parse(text)

open('wakati.txt', 'w').write( buff )
  
