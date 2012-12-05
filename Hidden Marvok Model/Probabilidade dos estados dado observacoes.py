################################################################
# Variação do problema 1                                       #
# Aqui estamos interessados em calcular                        #
# a probabilidade de uma certa sequencia                       #
# de estados, dada uma observação.                             #
# P(q1,q2,q3 | O1,O2,O3) = P(q1,q2,q3,O1,O2,O3) / P(O1,O2,O3)  #
# Data: 04/12/2012                                             #
################################################################

import math

SMALL = 0
MEDIUM = 1
LARGE = 2

COLD = 0
HOT = 1

pi = [0.5, 0.5]
A = [ [0.75,0.25],[0.4, 0.6] ]
B = [ [0.8, 0.1,0.1],[0.05,0.4,0.55] ]

O = "SMSL"
Qs = ["CCCC", "CCCH", "CCHC", "CCHH", "CHCC", "CHCH", "CHHC", "CHHH", "HCCC", "HCCH", "HCHC", "HCHH", "HHCC", "HHCH", "HHHC", "HHHH"]

temperatoraNoAno = [ [0 for x in range(len(pi))] for t in range(len(O)) ]

alpha = []

alpha.append([])
for i in range(2):
  if (O[0] == 'S'):
    Oi = SMALL
  elif (O[0] == 'M'):
    Oi = MEDIUM
  else:
    Oi = LARGE
  alpha[0].append(pi[i]*B[i][Oi])
  
for t in range(1,len(O)):
  if (O[t] == 'S'):
    Oi = SMALL
  elif (O[t] == 'M'):
    Oi = MEDIUM
  else:
    Oi = LARGE
  alpha.append([0,0])
  for j in range(2):
    sum = 0
    for i in range(2):
      sum += alpha[t-1][i] * A[i][j]
    alpha[t][j] = sum * B[j][Oi]

P = 0
for i in range(2):
  P += alpha[len(O)-1][i]

for Q in Qs:
  numerador = 0

  if (Q[0] == 'C'):
    q = COLD
  else:
    q = HOT  

  if (O[0] == 'S'):
    Oi = SMALL
  elif (O[0] == 'M'):
    Oi = MEDIUM
  else:
    Oi = LARGE
      
  numerador = pi[q]*B[q][Oi]
  q_anterior = q
  for t in range(1,len(Q)):
    if (Q[t] == 'C'):
      q = COLD
    else:
      q = HOT  
      
    if (O[t] == 'S'):
      Oi = SMALL
    elif (O[t] == 'M'):
      Oi = MEDIUM
    else:
      Oi = LARGE
      
    numerador *= A[q_anterior][q] * B[q][Oi]
    q_anterior = q
    
  resp = numerador / P 
	
  for t in range(len(Q)):
    if (Q[t] == 'C'):
      q = COLD
    else:
      q = HOT
      
    temperatoraNoAno[t][q] += resp
  
  print Q, "--", resp
  
print temperatoraNoAno