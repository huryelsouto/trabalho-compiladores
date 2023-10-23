class Gramatica(object):
    
    
    def __init__(self, V, T, P, S, epsilon=""):
        self.V = V
        self.T = T
        self.P = list(map(lambda p: (p[0], p[1].split(' ')), P))
        self.S = S
        self.vazia = epsilon
        
        self.fatorada = False
        
    
    def first(self, X):

        conj = set()
        
        if X in self.T:
            conj.add(X)
        else:
            if (X, self.vazia) in self.P:
                conj.add(self.vazia)

            # para todas producoes-p que possuem X na cabeca (X -> [...])
            for p in filter(lambda e: e[0] == X, self.P):
                Y = p[1] # tail

                for i in range(len(Y)):
                    if Y[i] in self.T:
                        conj.add(Y[i])
                        break
                    
                    # lista de bool: epsilon in FIRST(Yk), k = 0, ..., i-1
                    vazio_yk = map(lambda e: self.vazia in self.first(e), Y[:i])
                    
                    try:
                        # acha indice k do primeiro Yk tal que epsilon not in FIRST(Yk)
                        nexti = vazio_yk.index(False)
                        return conj.union(self.first(Y[nexti]))

                    # nao achou False in vazio_yk
                    except:
                        return conj.union(self.first(Y[i]))

        return conj



    def follow(self, A):
        conj = set()

        if A == self.S:
            conj.add("$")

        for p in self.P:
            B = p[0] # head
            t = p[1] # tail

            try:
                # indice de onde achou A em t (B -> t) (A in t)
                idx_A = t.index(A)
                beta = t[idx_A+1:]

                # nesse caso A estah por ultimo e diferente da cabeca
                if not beta and B != t[idx_A]:
                    conj = conj.union(self.follow(B))

                # se achou A no meio de t, une com FIRST do prox (primeiro de beta == beta[0]) - epsilon
                elif idx_A > 0 and idx_A < len(t)-1:
                    conj = conj.union(self.first(beta[0]).difference({self.vazia}))

                    # se epsilon in FIRST(prox), une com FOLLOW(prox)
                    if self.vazia in self.first(beta[0]):
                        conj = conj.union(self.follow(beta[0]))

            except:
                pass

        return conj


        



    def __str__(self):
        return "V = " + str(self.V) + "\nT = " + str(self.T) + "\nP = " + str(self.P) + "\nS = " + str(self.S)