from gensim.models.poincare import PoincareModel

import pickle

relations = pickle.loads(open('relations.pkl', 'rb').read())

model = PoincareModel(relations, size=2)

model.train(epochs=590)

open('model.pkl', 'wb').write( pickle.dumps(model) )
