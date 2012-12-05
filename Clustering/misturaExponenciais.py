import math

N = [7.8745,9.0244,0.11303,12.771,12.041,8.3501,8.2138,7.3548,16.631,6.984,1.3099,16.647,0.60308,0.19518,0.36838,0.34519,1.6955,1.1348,1.8215,0.29858,0.5679,0.29492,1.2456,2.3642,50.471,15.311,6.1094,6.3664,32.8233,4.3917,3.8202,3.3976,7.3414,12.589,21.353,6.2425,0.54136,2.4628,0.25492,0.34033,3.8651,1.5619,0.38951,0.79158,0.70681,1.0422,0.49119,0.78336]

# variacao minima para terminar o algoritmo
error = 0.00001

# condicoes iniciais
pi = [0.5, 0.5]
old_pi = [0.5, 0.5]

lambd = [0.1,0.5]
old_lambd = [0,0]

z = [ [ 0 for i in range(2) ] for j in range(len(N)) ]
exponential_memorization = [ [ -1 for i in range(2) ] for j in range(len(N)) ]

def reset_exponential_memorization():
  exponential_memorization = [ [ -1 for i in range(2) ] for j in range(len(N)) ]

def square(x):
  return math.pow(x,2)

def exponential_probability(n, k):
  if (exponential_memorization[n][k] == -1):
    x_n = N[n]
    lambda_k = lambd[k]
    exponential_memorization[n][k] = lambda_k * math.exp(-lambda_k * x_n)
    
  return exponential_memorization[n][k]

def expectation():
  reset_exponential_memorization()
  for n in range(len(N)):
    denominator = 0.0
    for j in range(2):
      denominator += pi[j] * exponential_probability(n,j)
    for k in range(2):
      z[n][k] = (pi[k] * exponential_probability(n,k)) / denominator
      
def maximization():
  lambd = [0,0]
  pi = [0,0]
  
  Nk = [0,0]
  for k in range(2):
    for n in range(len(N)):
      Nk[k] += z[n][k]
    
  # atualizar lambda
  for k in range(2):    
    for n in range(len(N)):
      lambd[k] += z[n][k] * N[n]
    lambd[k] = Nk[k] / lambd[k]
      
  # atualizar pi
  for k in range(2):
    pi[k] = Nk[k]/len(N)
    
  return (lambd, pi)

def goodEnough():
  for k in range(2):
    if ( (abs(lambd[k] - old_lambd[k]) > error) ):
      return False
      
  return True
  
while (not goodEnough()):
  expectation()
  old_lambd = lambd
  old_pi = pi
  lambd, pi = maximization()

print lambd
print pi