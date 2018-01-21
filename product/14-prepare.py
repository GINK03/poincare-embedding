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

buff = ''
for name in glob.glob('../../scraping-designs/rakuten-scrape/items/*'):
  obj = json.loads( open(name).read().lower() )

  text = obj['item'] + obj['desc']
  print(text)

