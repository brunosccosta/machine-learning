###############################
# Problema 1 conforme artigo  #
# P(O|M)                      #
# Data: 04/12/2012            #
###############################

import math

HEAD = 0
TAIL = 1

pi = [0.4, 0.6]
A = [ [0.8,0.2],[0.2, 0.8] ]
B = [ [0.9, 0.1],[0.1,0.9] ]

O = "HTHTHTHT"

alpha = []

alpha.append([])
for i in range(2):
  if (O[0] == 'H'):
    Oi = HEAD
  else:
    Oi = TAIL
  alpha[0].append(pi[i]*B[i][Oi])
  
for t in range(1,len(O)):
  if (O[t] == 'H'):
    Oi = HEAD
  else:
    Oi = TAIL
  alpha.append([0,0])
  for j in range(2):
    sum = 0
    for i in range(2):
      sum += alpha[t-1][i] * A[i][j]
    alpha[t][j] = sum * B[j][Oi]

P = 0
for i in range(2):
  P += alpha[len(O)-1][i]
  
print P
print alpha[len(O)-1]