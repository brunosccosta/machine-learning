from HMM import HMM

pi = [0.5, 0.5]
pi_linha = [0.0, 1.0]
A = [[0.5, 0.5], [0.5, 0.5]]
B = [[0.8, 0.2], [0.3, 0.7]]

hmm = HMM(A, B, pi)
hmm_linha = HMM(A, B, pi_linha)

observacoes = [0,0]
print "O|M: ", hmm.probabilidade_observacoes(observacoes)
print "O|M': ", hmm_linha.probabilidade_observacoes(observacoes)

print "T = 1"
estados = [0]
observacoes = [0]
numerador = hmm.probabilidade_estados_observacoes(estados, observacoes)