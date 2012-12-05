###########################################
# Implementação do Algortimo de Viterbi   #
# Sequencia de estados que maximiza       #
# a probabilidade da observação dada      #
# Data: 04/12/2012                        #
###########################################

import math

HEAD = 0
TAIL = 1

COIN_A = 0
COIN_B = 1

pi = [0.5, 0.5]
A = [ [0.8,0.2],[0.2, 0.8] ]
B = [ [0.9, 0.1],[0.1,0.9] ]

O = "HTHTHTHT"

delta = [[]]
psi = [[0,0]]

if (O[0] == 'H'):
  Oi = HEAD
else:
  Oi = TAIL
for i in range(2):
  delta[0].append(pi[i]*B[i][Oi])

print delta
  
for t in range(1,len(O)):
  if (O[t] == 'H'):
    Oi = HEAD
  else:
    Oi = TAIL
  delta.append([0,0])
  psi.append([0,0])
  
  for j in range(2):
    max_delta = -1
    max_psi = -1
    for i in range(2):
      delta_ji = delta[t-1][i] * A[i][j]
      print t, j, i, delta_ji
      if (delta_ji > max_delta):
        max_delta = delta_ji
        max_psi = i
    delta[t][j] = max_delta * B[j][Oi]
    psi[t][j] = max_psi

print delta
print psi
    
P = max(delta[len(O)-1])
Qt = delta[len(O)-1].index(P)

state_sequence = ''

if (Qt == COIN_A):
  state_sequence += 'A'
else:
  state_sequence += 'B'
  
for t in range(len(O)-1,0,-1):
  Qt = psi[t][Qt]
  if (Qt == COIN_A):
    state_sequence += 'A'
  else:
    state_sequence += 'B'
	
print state_sequence[::-1]