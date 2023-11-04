from AnalisadorLexico import AnalisadorLexico
from Gramatica import Gramatica
from Arvore import Arvore

class AnalisadorSintatico():


    def __init__(self, dir_automato, dir_arq, gramatica):
        self.lex = AnalisadorLexico(dir_automato, dir_arq)
        self.gramatica = gramatica
        self.proxToken = None
        self.arv = Arvore()
        

    # Descida Recursiva sem Retrocesso
    def drsr(self):
        self.proxToken = self.lex.__run__()
        prodA = self.gramatica.acha_adequada(self.proxToken)

        for Xi in prodA[1]:
            if Xi not in self.gramatica.terminal:
                # ativa o procedimento para Xi
                self.proc(Xi)()
            elif Xi == self.proxToken:
                self.proxToken = self.lex.__run__()
            else:
                self.trata_erro()

    # ativa o procedimento para Xi
    def proc(self, Xi):
        return {'S': self.S,
                'bloco': self.bloco,
                'dec_vars': self.dec_vars,
                'tipo': self.tipo,
                'seq_cmd': self.seq_cmd,
                'comment': self.comment,
                'cmd': self.cmd,
                'exp_arit': self.exp_arit,
                'exp_arit_termo': self.exp_arit_termo,
                'exp_arit_elev': self.exp_arit_elev,
                'exp_arit_fator': self.exp_arit_fator,
                'exp_rel': self.exp_rel,
                'exp_rel_and': self.exp_rel_and,
                'exp_rel_eq': self.exp_rel_eq,
                'exp_rel_comp': self.exp_rel_comp,
                'exp_rel_fator': self.exp_rel_fator,
                'constant_fator': self.constant_fator,
                'constant_char': self.constant_char,
                'constant_float': self.constant_float
                }[Xi]


    def S(self):
        if self.proxToken == 'function':
            self.proxToken = self.lex.__run__()

            if self.proxToken == 'id':
                self.proxToken = self.lex.__run__()

                if self.proxToken == '(':
                    self.proxToken = self.lex.__run__()

                    if self.proxToken == ')':
                        self.proxToken = self.lex.__run__()
                        self.proc('bloco')()
                    
                    else:
                        self.trata_erro(self, ')')

                else:
                    self.trata_erro(self, '(')

            else:
                self.trata_erro(self, 'id')

            self.proc(self.proxToken)()

        else:
            self.trata_erro(self, 'function')
            

    def bloco(self):
        pass


    def trata_erro(self):
        pass

    
    def trata_erro(self, tokens):
        raise Exception(f'Erro: {tokens} esperado(s) ({self.proxToken} encontrado)')
            

