
import pickle

relations = []
for line in open('dataset.txt'):
  line = line.strip()
  relation = line.split()
  relations.append( relation )

open('relations.pkl', 'wb').write( pickle.dumps(relations) )
