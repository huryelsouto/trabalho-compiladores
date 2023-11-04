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
        self.proxToken = self.lex.__prox_token__()
        prodA = self.gramatica.acha_adequada(self.proxToken)

        for Xi in prodA[1]:
            if Xi not in self.gramatica.terminal:
                # ativa o procedimento para Xi
                self.proc(Xi)()
            elif Xi == self.proxToken:
                self.proxToken = self.lex.__prox_token__()
            else:
                self.trata_erro()

    # ativa o procedimento para Xi
    def proc(self, Xi):
        return {'S': self.S,
                'bloco': self.bloco,
                'declare_vars': self.declare_vars,
                'tipo': self.tipo,
                'seq_cmd': self.seq_cmd,
                'comment': self.comment,
                'cmd': self.cmd,
                'exp_arit': self.exp_arit,
                'exp_arit_aux': self.exp_arit_aux,
                'exp_arit_termo': self.exp_arit_termo,
                'exp_arit_termo_aux': self.exp_arit_termo_aux,
                'exp_arit_elev': self.exp_arit_elev,
                'exp_arit_elev_aux': self.exp_arit_elev_aux,
                'exp_arit_fator': self.exp_arit_fator,
                'exp_rel': self.exp_rel,
                'exp_rel_aux': self.exp_rel_aux,
                'exp_rel_and': self.exp_rel_and,
                'exp_rel_and_aux': self.exp_rel_and_aux,
                'exp_rel_eq': self.exp_rel_eq,
                'exp_rel_eq_aux': self.exp_rel_eq_aux,
                'exp_rel_comp': self.exp_rel_comp,
                'exp_rel_comp_aux': self.exp_rel_comp_aux,
                'exp_rel_fator': self.exp_rel_fator,
                'constant_char': self.constant_char,
                'constant_int': self.constant_int,
                'constant_float': self.constant_float
                }[Xi]


    def S(self):
        if self.proxToken == 'program':
            self.proxToken = self.lex.__prox_token__()

            if self.proxToken == 'id':
                self.proxToken = self.lex.__prox_token__()

                if self.proxToken == '(':
                    self.proxToken = self.lex.__prox_token__()

                    if self.proxToken == ')':
                        self.proxToken = self.lex.__prox_token__()
                        self.proc('bloco')()
                    
                    else:
                        self.trata_erro(self, ')')

                else:
                    self.trata_erro(self, '(')

            else:
                self.trata_erro(self, 'id')

            self.proc(self.proxToken)()

        else:
            self.trata_erro(self, 'program')
            

    def bloco(self):
        pass


    def declare_vars(self):
        self.proc('tipo')()

        if self.proxToken == ':':
            self.proxToken = self.lex.__prox_token__()
            self.proc('lista_ids')()

            if self.proxToken == ';':
                self.proxToken = self.lex.__prox_token__()

            else:
                self.trata_erro(self, ';')

        else:
            self.trata_erro(self, ':')


    def tipo(self):
        if self.proxToken in ['int', 'char', 'float']:
            self.proxToken = self.lex.__prox_token__()
        
        else:
            self.trata_erro(self, str(['int', 'char', 'float']))


    # tá meio errado conferir
    def lista_ids(self):
        if self.proxToken == 'id':
            self.proxToken = self.lex.__prox_token__()

            if self.proxToken == ',':
                self.proxToken = self.lex.__prox_token__()
                self.proc('lista_ids')()

            else:
                self.trata_erro(self, ',')

        else:
            self.trata_erro(self, 'id')


    def comment(self):
        if self.proxToken == '{':
            self.proxToken = self.lex.__prox_token__()

            while self.proxToken != '}':
                self.proxToken = self.lex.__prox_token__()

            if self.proxToken == '}':
                self.proxToken = self.lex.__prox_token__()

            else:
                self.trata_erro(self, '}')

        else:
            self.trata_erro(self, '{')

    
    def seq_cmd(self):
        pass


    def cmd(self):
        pass


    def exp_arit(self):
        self.proc('exp_arit_termo')()
        self.proc('exp_arit_aux')()

    
    def exp_arit_aux(self):
        pass


    def exp_arit_termo(self):
        self.proc('exp_arit_elev')()
        self.proc('exp_arit_termo_aux')()


    def exp_arit_termo_aux(self):
        pass


    def exp_arit_elev(self):
        self.proc('exp_arit_fator')()
        self.proc('exp_arit_elev_aux')()


    def exp_arit_elev_aux(self):
        pass


    def exp_arit_fator(self):
        pass


    def exp_rel(self):
        self.proc('exp_rel_and')()
        self.proc('exp_rel_aux')()


    def exp_rel_aux(self):
        pass


    def exp_rel_and(self):
        self.proc('exp_rel_eq')()
        self.proc('exp_rel_and_aux')()


    def exp_rel_and_aux(self):
        pass


    def exp_rel_eq(self):
        self.proc('exp_rel_comp')()
        self.proc('exp_rel_eq_aux')()


    def exp_rel_eq_aux(self):
        pass


    def exp_rel_comp(self):
        self.proc('exp_rel_fator')()
        self.proc('exp_rel_comp_aux')()

    
    def exp_rel_comp_aux(self):
        pass


    def exp_rel_fator(self):
        pass


    def constant_char(self):
        pass


    def constant_int(self):
        pass


    def constant_float(self):
        pass


    def trata_erro(self):
        pass

    
    def trata_erro(self, tokens):
        raise Exception(f'Erro: {tokens} esperado(s) ({self.proxToken} encontrado)')
            

