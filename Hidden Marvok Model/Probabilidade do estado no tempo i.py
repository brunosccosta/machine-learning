################################
# Problema 2 conforme artigo   #
# \gama_i(t) = P(q_t = S_i|O,M)#
# Data: 04/12/2012             #
################################

import math

HEAD = 0
TAIL = 1

pi = [0.5, 0.5]
A = [ [0.8,0.2],[0.2, 0.8] ]
B = [ [0.9, 0.1],[0.1,0.9] ]

O = "HTH"

alpha = []
beta = [ [ 0 for i in range(2) ] for j in range(len(O)) ]
gama = [ [ 0 for i in range(2) ] for j in range(len(O)) ]

#calculando alpha
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

#calculando beta
for i in range(2):
  beta[len(O) -1][i] = 1

for t in range(len(O)-2,0,-1):
  if (O[t+1] == 'H'):
    Oi = HEAD
  else:
    Oi = TAIL
  for i in range(2):
    sum = 0
    for j in range(2):
      sum += A[i][j] * B[j][Oi] * beta[t+1][j]
    beta[t][i] = sum 
  
#calculando gama
denominador = 0
for i in range(2):
  denominador += alpha[len(O)-1][i]

for t in range(1,len(O)):
  for i in range(2):
    gama[t][i] = (alpha[t][i] * beta[t][i]) / denominador
  
print gama