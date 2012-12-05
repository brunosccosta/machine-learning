import math

N = [7.8745,9.0244,0.11303,12.771,12.041,8.3501,8.2138,7.3548,16.631,6.984,1.3099,16.647,0.60308,0.19518,0.36838,0.34519,1.6955,1.1348,1.8215,0.29858,0.5679,0.29492,1.2456,2.3642,50.471,15.311,6.1094,6.3664,32.8233,4.3917,3.8202,3.3976,7.3414,12.589,21.353,6.2425,0.54136,2.4628,0.25492,0.34033,3.8651,1.5619,0.38951,0.79158,0.70681,1.0422,0.49119,0.78336]

# variacao minima para terminar o algoritmo
error = 0.00001

# condicoes iniciais
pi = [0.5, 0.5]
old_pi = [0.5, 0.5]

mi = [0,10]
old_mi = [0,0]

sigma = [1,5]
old_sigma = [0,0]

z = [ [ 0 for i in range(2) ] for j in range(len(N)) ]
gaussian_memorization = [ [ -1 for i in range(2) ] for j in range(len(N)) ]

def reset_gaussian_memorization():
  gaussian_memorization = [ [ -1 for i in range(2) ] for j in range(len(N)) ]

def square(x):
  return math.pow(x,2)

def gaussian_probability(n, k):
  if (gaussian_memorization[n][k] == -1):
    sigma_k = sigma[k]
    x_n = N[n]
    mi_k = mi[k]
    gaussian_memorization[n][k] = math.exp(-square(x_n - mi_k)/(2*sigma_k))/math.sqrt(2*math.pi*sigma_k)
    
  return gaussian_memorization[n][k]

def expectation():
  reset_gaussian_memorization()
  for n in range(len(N)):
    for k in range(2):        
      denominator = 0.0
      for j in range(2):
        denominator += pi[j] * gaussian_probability(n,j)
            
      z[n][k] = (pi[k] * gaussian_probability(n,k)) / denominator
      
def maximization():
  mi = [0,0]
  sigma = [0,0]
  pi = [0,0]
  
  Nk = [0,0]
  for k in range(2):
    for n in range(len(N)):
      Nk[k] += z[n][k]
    
  # atualizar mi
  for k in range(2):    
    for n in range(len(N)):
      mi[k] += z[n][k] * N[n]
    mi[k] /= Nk[k]
  
  # atualizar sigma
  for k in range(2):    
    for n in range(len(N)):
      sigma[k] += z[n][k] * square(N[n] - mi[k])
    sigma[k] /= Nk[k]
    
  # atualizar pi
  for k in range(2):
    pi[k] = Nk[k]/len(N)
    
  return (mi, sigma, pi)

def goodEnough():
  for k in range(2):
    if ( (abs(mi[k] - old_mi[k]) > error) ):
      return False
    
    if ( (abs(sigma[k] - old_sigma[k]) > error) ):
      return False
      
  return True
  
while (not goodEnough()):
  expectation()
  old_mi = mi
  old_sigma = sigma
  old_pi = pi
  mi, sigma, pi = maximization()

print mi
print [ math.sqrt(x) for x in sigma ]
print pi