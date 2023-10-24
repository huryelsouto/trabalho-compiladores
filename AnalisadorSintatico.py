from AnalisadorLexico import AnalisadorLexico
from Gramatica import Gramatica

class AnalisadorSintatico():


    def __init__(self, dir_automato, dir_arq, gramatica):
        self.lex = AnalisadorLexico(dir_automato, dir_arq)
        self.gramatica = gramatica
        

    # Descida Recursiva sem Retrocesso
    def drsr(self):
        proxToken = self.lex.__run__()
        prodA = self.gramatica.acha_adequada(proxToken)

        for Xi in prodA[1]:
            if Xi not in self.gramatica.terminal:
                # ativa o procedimento para Xi
                self.proc(Xi)
            elif Xi == proxToken:
                proxToken = self.lex.__run__()
            else:
                self.trata_erro()

    # ativa o procedimento para Xi
    def proc(self, Xi):
        pass

    
    def trata_erro(self):
        pass
            

