import json
import copy

class Gramatica(object):
    
    
    def __init__(self, V, T, P, S, epsilon="", eof="$"):
        self.V = V
        self.T = T
        self.P = list(map(lambda p: (p[0], p[1].split(' ')), P))
        self.S = S

        self.vazia = epsilon
        self.eof = eof

        self.firsts = dict()
        self.follows = dict()
        
        self.fatorada = False

    @classmethod
    def from_json(self, dir_json, epsilon="", eof="$"):
        f = open(dir_json)
        j = json.load(f)
        return Gramatica(j["V"], j["T"], j["P"], j["S"], epsilon=epsilon, eof=eof)


    def acha_adequada(self, A):
        prodA = None
        for p in self.P:
            if p[0] == A:
                prodA = p
                break
        return prodA

        
    def first(self, X):
        if X not in self.firsts:
            self.firsts.update({X: self.__first__(X)})

        return self.firsts[X]

    
    def __first__(self, X):

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
        if A not in self.follows:
            self.follows.update({A: self.__follow__(A)})

        return self.follows[A]


    def __follow__(self, A):
        conj = set()

        if A == self.S:
            conj.add(self.eof)

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


    # encontra producoes-A com prefixo comum
    def __encontra_pApc__(self):
        equivs = []
        
        for i in range(len(self.P)-1):
            p = self.P[i]
            
            equivs.append((p, []))
            
            # se producao ainda nao foi "equivalecionada"
            #if p not in equivs:
            #    equivs.append((p, []))
                
            for j in range(i+1, len(self.P)):
                q = self.P[j]
                
                if i == j:
                    continue
                
                # conta tamanho do prefixo igual das producoes p e q
                count = 0
                
                menor = p[1] if len(p[1]) < len(q[1]) else q[1]
                maior = p[1] if len(p[1]) >= len(q[1]) else q[1]
                for a in range(len(menor)):
                        if maior[a] == menor[a]:
                            count += 1
                        else:
                            break
                
                # se contador de tamanho > 0, possuem prefixo comum
                if count > 0:                       
                    # adiciona na lista de equivalencia de p (ultima tupla colocada) 
                    equivs[-1][1].append((count, q))                    
            
        return list(filter(lambda e: e[1], equivs))
    
    
    # encontra prefixo mais longo alpha comum a 2 ou mais producoes-A
    def __pApcl__(self, pApc):
        
        maior = 0
        alpha = None
        
        for p, equivs in pApc:
            for count, q in equivs:
                maior = count if count > maior else maior
                alpha = q[1][:maior] if count == maior else alpha

        if len(alpha) == 1 and alpha[0] == self.vazia:
            alpha = None
                
        return alpha
        
           
    def fatorar_gramatica(self):
        if self.fatorada:
            return False
        
        for A in self.V:
            pApc = self.__encontra_pApc__() # producoes-A com prefixo comum
            print("A=", A)
            print("pApc=", pApc)
            while pApc:
                alpha = self.__pApcl__(pApc) 
                print("alpha=", alpha)
                print("alpha is not None", alpha is not None)
                # se alpha != epsilon
                if alpha is not None:
                    
                    print(f"\n----\nself\n----\n")
                    betas = []
                    p_remover = []
                    
                    # filtra para producoes-A (A -> w)
                    for p in filter(lambda e: e[0] == A, self.P):
                        
                        # corpo comecando por alpha
                        if p[1][:len(alpha)] == alpha:
                    
                            betas.append(p[1][len(alpha):])
                            p_remover.append(p)
                    
                    # removendo producoes-A que começam por alpha (A -> alpha beta1 | ... | alpha betan)
                    for pr in p_remover:
                        self.P.remove(pr)
                    
                    # criando o corpo: alpha A' (ou A'', A''', ...)
                    A_linha = A
                    while A_linha in self.V:
                        A_linha = A_linha + '\''
                        
                    alpha_A_linha = ''
                    for a in alpha:
                        if a != self.vazia:
                            alpha_A_linha = alpha_A_linha + a

                    print("alpha=", alpha)
                    print("A_linha=", A_linha)
                    alpha_A_linha = alpha_A_linha + A_linha
                    
                    print("(A, alpha_A_linha)=", (A, alpha_A_linha))
                    self.P.append((A, alpha_A_linha))
                    
                    for bi in betas:
                        self.P.append((A_linha, bi))
                        
                    print("betas=",betas)
                    print("p_remover=",p_remover)
                    print("alpha_A_linha=",alpha_A_linha)
                    
        self.fatorada = True
        return True

    def __str__(self):
        return "V = " + str(self.V) + "\nT = " + str(self.T) + "\nP = " + str(self.P) + "\nS = " + str(self.S)