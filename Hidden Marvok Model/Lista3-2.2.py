from HMM import HMM

pi = [0.5, 0.5]
A = [[0.5, 0.5], [0.5, 0.5]]
B = [[0.8, 0.2], [0.3, 0.7]]

hmm = HMM(A, B, pi)

observations_head = [0,0,0,1,1,0,0]
print "Head: ", hmm.probabilidade_observacoes(observations_head)

observations_tail = [0,0,0,1,1,0,1]
print "Tail: ", hmm.probabilidade_observacoes(observations_tail)