import numpy as np
from sklearn import hmm

prng = np.random.RandomState(9)

##############################################################
n_components = 3 # ('Urna A', 'Urna B', 'Urna C')
n_symbols = 3  # ('Bola Red', 'Bola Blue', 'Bola Green')
emissionprob = [[0.34, 0.33, 0.33], [0.4, 0.55, 0.05], [0.05, 0.55, 0.4]]
startprob = [0.34, 0.33, 0.33]
transmat = [[0.34, 0.33, 0.33], [0.9, 0.05, 0.05], [0.9, 0.05, 0.05]]
 
h = hmm.MultinomialHMM(n_components,
                   startprob=startprob,
                   transmat=transmat)
h.emissionprob = emissionprob

observations = [1, 1, 2, 2, 1, 0, 1, 2, 2, 0]

h.fit(observations, n_iter=2)
 
print h.startprob
