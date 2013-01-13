################################
# HMM Class                    #
# Problema 1 e 2 implementados #
# Data: 13/01/2013             #
################################

import math

class HMM:
  def __init__(self, A, B, pi):
    self.A = A
    self.B = B
    self.pi = pi
    self._estados = len(A)
  
  def probabilidade_observacoes(self, observacoes):
    alpha = []

    alpha.append([])
    for i in range(self._estados):
      alpha[0].append(self.pi[i]*self.B[i][observacoes[0]])
      
    for t in range(1,len(observacoes)):
      Ot = observacoes[t]
      alpha.append([0,0])
      for j in range(self._estados):
        sum = 0
        for i in range(2):
          sum += alpha[t-1][i] * self.A[i][j]
        alpha[t][j] = sum * self.B[j][Ot]

    probabilidade = 0
    for i in range(self._estados):
      probabilidade += alpha[len(observacoes)-1][i]
  
    return probabilidade

  def viterbi(self, observacoes):
    psi = [ [0 for i in range(self._estados)] ]
    delta = [[]]

    for i in range(self._estados):
      delta[0].append(self.pi[i]*self.B[i][observacoes[0]])
     
    for t in range(1,len(observacoes)):
      Ot = observacoes[t]
      delta.append( [0 for i in range(self._estados)] )
      psi.append( [0 for i in range(self._estados)] )
      
      for j in range(self._estados):
        max_delta = -1
        max_psi = -1
        for i in range(self._estados):
          delta_ji = delta[t-1][i] * self.A[i][j]
          if (delta_ji > max_delta):
            max_delta = delta_ji
            max_psi = i
        delta[t][j] = max_delta * self.B[j][Ot]
        psi[t][j] = max_psi
        
    P = max(delta[len(observacoes)-1])
    Qt = delta[len(observacoes)-1].index(P)

    state_sequence = str(Qt)
      
    for t in range(len(observacoes)-1,0,-1):
      Qt = psi[t][Qt]
      state_sequence += str(Qt)
      
    return state_sequence[::-1]
    
  def probabilidade_estados_observacoes(self, estados, observacoes):
    P = 0
    q = estados[0]
    
    P = self.pi[q] * self.B[q][observacoes[0]]
    q_anterior = q
    for t in range(1,len(estados)):
      q = estados[t]
      Oi = observacoes[t]
      
      P *= self.A[q_anterior][q] * self.B[q][Oi]
      q_anterior = q
      
    return P