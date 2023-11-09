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
                        self.trata_erro(')')

                else:
                    self.trata_erro('(')

            else:
                self.trata_erro('id')

            self.proc(self.proxToken)()

        else:
            self.trata_erro('program')
            

    def bloco(self):
        if self.proxToken == '{':
            self.proxToken = self.lex.__prox_token__()

            atual = self.lex.get_pos()
            try:
                self.proc('declare_vars')()

            except:
                self.lex.rollback(atual)
                self.proc('seq_cmd')()

                if self.proxToken == '}':
                    self.proxToken == self.lex.__prox_token__()

                else:
                    self.trata_erro('}')

            if self.proxToken == ',':
                self.proxToken = self.lex.__prox_token__()

                self.proc('seq_cmd')

                if self.proxToken == '}':
                    self.proxToken = self.lex.__prox_token__()

                else:
                    self.trata_erro('}')

            else:
                self.trata_erro(',')



    def declare_vars(self):
        self.proc('tipo')()

        if self.proxToken == ':':
            self.proxToken = self.lex.__prox_token__()
            self.proc('lista_ids')()

            if self.proxToken == ';':
                self.proxToken = self.lex.__prox_token__()

            else:
                self.trata_erro(';')

        else:
            self.trata_erro(':')


    def tipo(self):
        if self.proxToken in ['int', 'char', 'float']:
            self.proxToken = self.lex.__prox_token__()
        
        else:
            self.trata_erro(str(['int', 'char', 'float']))


    def lista_ids(self):
        if self.proxToken == 'id':
            self.proxToken = self.lex.__prox_token__()
            
            if self.proxToken == ',':
                self.proc('lista_ids')()

        else: 
            self.trata_erro('id')


    def comment(self):
        if self.proxToken == '{':
            self.proxToken = self.lex.__prox_token__()

            while self.proxToken != '}':
                self.proxToken = self.lex.__prox_token__()

            if self.proxToken == '}':
                self.proxToken = self.lex.__prox_token__()

            else:
                self.trata_erro('}')

        else:
            self.trata_erro('{')

    
    def seq_cmd(self):
        self.proc('cmd')()

        atual = self.lex.get_pos()
        try:
            self.proc('seq_cmd')()
        
        except:
            self.lex.rollback(atual)



    def cmd(self):
        if self.proxToken == 'id':
            self.proxToken = self.lex.__prox_token__()

            if self.proxToken == ':=':
                self.proxToken = self.lex.__prox_token__()

                atual = self.lex.get_pos()
                try:
                    self.proc('exp_arit')()

                except:
                    self.lex.rollback(atual)
                    self.proc('exp_rel')()

                if self.proxToken == ';':
                    self.proxToken = self.lex.__prox_token__()

                    



    def exp_arit(self):
        self.proc('exp_arit_termo')()
        self.proc('exp_arit_aux')()

    
    def exp_arit_aux(self):
        if self.proxToken in ['+', '-']:
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_arit_termo')()
            self.proc('exp_arit_aux')()
        

    def exp_arit_termo(self):
        self.proc('exp_arit_elev')()
        self.proc('exp_arit_termo_aux')()


    def exp_arit_termo_aux(self):
        if self.proxToken in ['*', '/']:
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_arit_elev')()
            self.proc('exp_arit_termo_aux')()


    def exp_arit_elev(self):
        self.proc('exp_arit_fator')()
        self.proc('exp_arit_elev_aux')()


    def exp_arit_elev_aux(self):
        if self.proxToken == '^':
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_arit_fator')()
            self.proc('exp_arit_elev_aux')()


    def exp_arit_fator(self):
        atual = self.lex.get_pos()

        try:
            self.proc('constant_char')()
        
        except:
            self.lex.rollback(atual)

            try:
                self.proc('constant_int')()

            except:
                self.lex.rollback(atual)

                try:
                    self.proc('constant_float')()

                except:
                    self.lex.rollback(atual)

                    if self.proxToken == '(':
                        self.proxToken = self.lex.__prox_token__()

                        self.proc('exp_arit')()

                        if self.proxToken == ')':
                            self.proxToken = self.lex.__prox_token__()

                        else:
                            self.trata_erro(')')
                    
                    else:
                        self.trata_erro('(')


    def exp_rel(self):
        self.proc('exp_rel_and')()
        self.proc('exp_rel_aux')()


    def exp_rel_aux(self):
        if self.proxToken == '|':
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_rel_and')()
            self.proc('exp_rel_aux')()


    def exp_rel_and(self):
        self.proc('exp_rel_eq')()
        self.proc('exp_rel_and_aux')()


    def exp_rel_and_aux(self):
        if self.proxToken == '&':
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_rel_eq')()
            self.proc('exp_rel_and_aux')()


    def exp_rel_eq(self):
        self.proc('exp_rel_comp')()
        self.proc('exp_rel_eq_aux')()


    def exp_rel_eq_aux(self):
        if self.proxToken in ['=', '!=']:
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_rel_comp')()
            self.proc('exp_rel_eq_aux')()


    def exp_rel_comp(self):
        self.proc('exp_rel_fator')()
        self.proc('exp_rel_comp_aux')()

    
    def exp_rel_comp_aux(self):
        if self.proxToken in ['>', '<', '<=', '>=']:
            self.proxToken = self.lex.__prox_token__()
            self.proc('exp_rel_fator')()
            self.proc('exp_rel_comp_aux')()


    def exp_rel_fator(self):
        atual = self.lex.get_pos()

        try:
            self.proc('constant_char')()
        
        except:
            self.lex.rollback(atual)

            try:
                self.proc('constant_int')()

            except:
                self.lex.rollback(atual)

                try:
                    self.proc('constant_float')()

                except:
                    self.lex.rollback(atual)

                    if self.proxToken == '(':
                        self.proxToken = self.lex.__prox_token__()

                        self.proc('exp_rel')()

                        if self.proxToken == ')':
                            self.proxToken = self.lex.__prox_token__()

                        else:
                            self.trata_erro(')')
                    
                    else:
                        self.trata_erro('(')


    def constant_char(self):
        if self.proxToken == '\'':
            self.proxToken = self.lex.__prox_token__()
            
            if self.proxToken != '\'':
                self.proxToken = self.lex.__prox_token__()
                self.proc('constant_char')()

            else:
                self.trata_erro('^\'')       
        
        
        else:
            self.trata_erro('\'')



    def constant_int(self):
        num = ['0','1','2','3','4','5','6','7','8','9']

        if self.proxToken in num:
            self.proxToken = self.lex.__prox_token__()

            while self.proxToken in num:
                self.proxToken = self.lex.__prox_token__()

        else:
            self.trata_erro(str(num))


    def constant_float(self):
        self.proc('constant_int')()

        if self.proxToken == '.':
            self.proxToken = self.lex.__prox_token__()

            self.proc('constant_int')()

            if self.proxToken == 'E':
                self.proxToken = self.lex.__prox_token__()

                if self.proxToken in ['+', '-']:
                    self.proxToken = self.lex.__prox_token__()

                self.proc('constant_int')

        else:
            self.trata_erro('.')



    def trata_erro(self):
        pass

    
    def trata_erro(self, tokens):
        raise Exception(f'Erro: {tokens} esperado(s) ({self.proxToken} encontrado)')
            

