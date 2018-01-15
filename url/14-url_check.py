
import json

import hashlib

sha_urls = json.loads(open('sha_urls.json').read())

shajp = set()

sha_url = {}
for _, urls in sha_urls.items():
  for url in urls:
    sha_url[ hashlib.sha256(bytes(url,'utf8')).hexdigest() ] = url

# remove  no use key
for sha in list(sha_urls.keys()):
  if sha not in sha_url:
    del sha_urls[sha]
    print(sha)

# top 30件を取り出す
url_freq = {}
for sha, urls in sha_urls.items():
  for url in urls:
    if url_freq.get(url) is None:
      url_freq[url] = 0
    url_freq[url] += 1
topN = { url for url, freq in sorted(url_freq.items(), key=lambda x:x[1]*-1)[:30] }


relations = []
for sha, urls in sha_urls.items():
  key_url = sha_url[sha]
  if key_url not in topN:
    continue
  for url in urls:
    if url not in topN:
      continue
    relations.append( (key_url, url) )
import pickle
open('relations.pkl', 'wb').write( pickle.dumps(relations) )
  

