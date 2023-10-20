class Gramatica(object):
    
    
    def __init__(self, V, T, P, S):
        self.V = V
        self.T = T
        self.P = list(map(lambda p: (p[0], p[1].split(' ')), P))
        self.S = S
        
        self.fatorada = False
        
    
    def first(self, A):

        conj = set()
        
        while True:
            for p in self.P:


    def follow(self, A):
        conj = set()

        if A == self.S:
            conj.add("$")

        for p in self.P:
            t = p[1] #tail

            try:
                idx_A = t.index(A)

                if idx_A > 0 and idx_A < len(t)-1:
                    beta = str(t[idx_A+1:]).replace('[', '').replace(',', '').replace('\'', '').replace(']', '')
                    conj.add(self.first(beta).difference(""))
                
                elif idx_A > 0 and idx_A == len(t)-1:
                    beta = str(t[idx_A+1:]).replace('[', '').replace(',', '').replace('\'', '').replace(']', '')

            if A in t and 


        



    def __str__(self):
        return "V = " + str(self.V) + "\nT = " + str(self.T) + "\nP = " + str(self.P) + "\nS = " + str(self.S)