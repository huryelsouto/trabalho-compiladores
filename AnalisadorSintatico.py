from AnalisadorLexico import AnalisadorLexico
from Gramatica import Gramatica
from Token import Token

class AnalisadorSintatico():


    def __init__(self, dir_automato, dir_arq, gramatica):
        self.lex = AnalisadorLexico(dir_automato, dir_arq)
        self.gramatica = gramatica
        self.proxToken = None
        

    # Descida Recursiva sem Retrocesso
    def drsr(self):
        self.proxToken = self.lex.prox_token()
        prodA = self.gramatica.acha_adequada(self.proxToken)

        
        for Xi in prodA[1]:
            print('Xi=', Xi)
            if Xi not in self.gramatica.T:
                # ativa o procedimento para Xi
                self.procedimento(Xi.nome)
    
            elif Xi == self.proxToken:
                self.proxToken = self.lex.prox_token()
            else:
                self.trata_erro(self.proxToken)


    # ativa o procedimento para Xi
    def proc(self, Xi):
        return {'S': self.S,
                'bloco': self.bloco,
                'declare_vars': self.declare_vars,
                'tipo': self.tipo,
                'seq_cmd': self.seq_cmd,
                'lista_ids': self.lista_ids,
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


    def procedimento(self, Xi):
        self.proc(Xi)()


    def S(self):
        if self.proxToken.nome == 'program':
            self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == 'id':
                self.proxToken = self.lex.prox_token()

                if self.proxToken.nome == '(':
                    self.proxToken = self.lex.prox_token()

                    if self.proxToken.nome == ')':
                        self.proxToken = self.lex.prox_token()
                        self.procedimento('bloco')
                    
                    else:
                        self.trata_erro(')')

                else:
                    self.trata_erro('(')

            else:
                self.trata_erro('id')

            self.procedimento(self.proxToken)

        else:
            self.trata_erro('program')
            

    def bloco(self):
        if self.proxToken.nome == 'begin':
            self.proxToken = self.lex.prox_token()

            atual = self.lex.get_pos()
            try:
                self.procedimento('declare_vars')

            except:
                self.lex.rollback(atual)
                self.procedimento('seq_cmd')

                if self.proxToken.nome == 'end':
                    self.proxToken == self.lex.prox_token()

                else:
                    self.trata_erro('end')

            if self.proxToken.nome == ',':
                self.proxToken = self.lex.prox_token()

                self.procedimento('seq_cmd')

                if self.proxToken.nome == 'end':
                    self.proxToken = self.lex.prox_token()

                else:
                    self.trata_erro('end')

            else:
                self.trata_erro(',')



    def declare_vars(self):
        self.procedimento('tipo')

        if self.proxToken.nome == ':':
            self.proxToken = self.lex.prox_token()
            self.procedimento('lista_ids')

            if self.proxToken.nome == ';':
                self.proxToken = self.lex.prox_token()

            else:
                self.trata_erro(';')

        else:
            self.trata_erro(':')


    def tipo(self):            
        if self.proxToken.atributo in ['int', 'char', 'float']:
            self.proxToken = self.lex.prox_token()

        else:
            self.trata_erro(str(['int', 'char', 'float']))


    def lista_ids(self):
        if self.proxToken.nome == 'id':
            self.proxToken = self.lex.prox_token()
            
            
            if self.proxToken.nome == ',':
                self.proxToken = self.lex.prox_token()
                self.procedimento('lista_ids')

        else: 
            self.trata_erro('id')


    def comment(self):
        if self.proxToken.nome == '{':
            self.proxToken = self.lex.prox_token()

            while self.proxToken != '}':
                self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == '}':
                self.proxToken = self.lex.prox_token()

            else:
                self.trata_erro('}')

        else:
            self.trata_erro('{')

    
    def seq_cmd(self):
        self.procedimento('cmd')

        atual = self.lex.get_pos()
        try:
            self.procedimento('seq_cmd')
        
        except:
            self.lex.rollback(atual)



    def cmd(self):
        if self.proxToken.nome == 'id':
            self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == ':=':
                self.proxToken = self.lex.prox_token()

                atual = self.lex.get_pos()
                try:
                    self.procedimento('exp_arit')

                except:
                    self.lex.rollback(atual)
                    self.procedimento('exp_rel')

                if self.proxToken.nome == ';':
                    self.proxToken = self.lex.prox_token()

        elif self.proxToken.nome == 'if':
            self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == '(':
                self.proxToken = self.lex.prox_token()
                
                self.procedimento('exp_rel')

                if self.proxToken.nome == ')':
                    self.proxToken = self.lex.prox_token()

                    self.procedimento('cmd')

                    if self.proxToken.nome == 'else':
                        self.proxToken = self.lex.prox_token()

                        self.procedimento('cmd')


                else:
                    self.trata_erro(')')
                
            else:
                self.trata_erro('(')

        elif self.proxToken.nome == 'while':
            self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == '(':
                self.proxToken = self.lex.prox_token()

                self.procedimento('exp_rel')

                if self.proxToken.nome == ')':
                    self.proxToken = self.lex.prox_token()

                    self.procedimento('cmd')
                
                else:
                    self.trata_erro(')')
            
            else:
                self.trata_erro(')')

        elif self.proxToken.nome == 'repeat':
            self.proxToken = self.lex.prox_token()

            self.procedimento('cmd')

            if self.proxToken.nome == 'until':
                self.proxToken = self.lex.prox_token()

                if self.proxToken.nome == '(':
                    self.proxToken = self.lex.prox_token()

                    self.procedimento('exp_rel')

                    if self.proxToken.nome == ')':
                        self.proxToken = self.lex.prox_token()

                        if self.proxToken.nome == ';':
                            self.proxToken = self.lex.prox_token()

                        else:
                            self.trata_erro(';')

                    else:
                        self.trata_erro(')')

                else:
                    self.trata_erro('(')

            else: 
                self.trata_erro('until')

        elif self.proxToken.nome == 'begin':
            self.proxToken = self.lex.prox_token()

            if self.proxToken.nome == '(':
                self.proxToken = self.lex.prox_token()

                self.procedimento('declare_vars')

                self.procedimento('cmd')

                if self.proxToken.nome == ')':
                    self.proxToken = self.lex.prox_token()

                    if self.proxToken.nome == 'end':
                        self.proxToken = self.lex.prox_token()

                    else:
                        self.trata_erro('end')

                else:
                    self.trata_erro(')')

            else:
                self.trata_erro('(')

        else:
            self.trata_erro(str(['id', 'if', 'while', 'repeat', 'begin']))

                    
    def exp_arit(self):
        self.procedimento('exp_arit_termo')
        self.procedimento('exp_arit_aux')

    
    def exp_arit_aux(self):
        if self.proxToken.nome in ['+', '-']:
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_arit_termo')
            self.procedimento('exp_arit_aux')
        

    def exp_arit_termo(self):
        self.procedimento('exp_arit_elev')
        self.procedimento('exp_arit_termo_aux')


    def exp_arit_termo_aux(self):
        if self.proxToken.nome in ['*', '/']:
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_arit_elev')
            self.procedimento('exp_arit_termo_aux')


    def exp_arit_elev(self):
        self.procedimento('exp_arit_fator')
        self.procedimento('exp_arit_elev_aux')


    def exp_arit_elev_aux(self):
        if self.proxToken.nome == '^':
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_arit_fator')
            self.procedimento('exp_arit_elev_aux')


    def exp_arit_fator(self):
        atual = self.lex.get_pos()

        try:
            self.procedimento('constant_char')
        
        except:
            self.lex.rollback(atual)

            try:
                self.procedimento('constant_int')

            except:
                self.lex.rollback(atual)

                try:
                    self.procedimento('constant_float')

                except:
                    self.lex.rollback(atual)

                    if self.proxToken.nome == '(':
                        self.proxToken = self.lex.prox_token()

                        self.procedimento('exp_arit')

                        if self.proxToken.nome == ')':
                            self.proxToken = self.lex.prox_token()

                        else:
                            self.trata_erro(')')
                    
                    else:
                        self.trata_erro('(')


    def exp_rel(self):
        self.procedimento('exp_rel_and')
        self.procedimento('exp_rel_aux')


    def exp_rel_aux(self):
        if self.proxToken.nome == '|':
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_rel_and')
            self.procedimento('exp_rel_aux')


    def exp_rel_and(self):
        self.procedimento('exp_rel_eq')
        self.procedimento('exp_rel_and_aux')


    def exp_rel_and_aux(self):
        if self.proxToken.nome == '&':
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_rel_eq')
            self.procedimento('exp_rel_and_aux')


    def exp_rel_eq(self):
        self.procedimento('exp_rel_comp')
        self.procedimento('exp_rel_eq_aux')


    def exp_rel_eq_aux(self):
        if self.proxToken.nome in ['=', '!=']:
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_rel_comp')
            self.procedimento('exp_rel_eq_aux')


    def exp_rel_comp(self):
        self.procedimento('exp_rel_fator')
        self.procedimento('exp_rel_comp_aux')

    
    def exp_rel_comp_aux(self):
        if self.proxToken.nome in ['>', '<', '<=', '>=']:
            self.proxToken = self.lex.prox_token()
            self.procedimento('exp_rel_fator')
            self.procedimento('exp_rel_comp_aux')


    def exp_rel_fator(self):
        atual = self.lex.get_pos()

        try:
            self.procedimento('constant_char')
        
        except:
            self.lex.rollback(atual)

            try:
                self.procedimento('constant_int')

            except:
                self.lex.rollback(atual)

                try:
                    self.procedimento('constant_float')

                except:
                    self.lex.rollback(atual)

                    if self.proxToken.nome == '(':
                        self.proxToken = self.lex.prox_token()

                        self.procedimento('exp_rel')

                        if self.proxToken.nome == ')':
                            self.proxToken = self.lex.prox_token()

                        else:
                            self.trata_erro(')')
                    
                    else:
                        self.trata_erro('(')


    def constant_char(self):
        if self.proxToken.nome == '\'':
            self.proxToken = self.lex.prox_token()
            
            if self.proxToken.nome != '\'':
                self.proxToken = self.lex.prox_token()
                self.procedimento('constant_char')

            else:
                self.trata_erro('^\'')       
        
        
        else:
            self.trata_erro('\'')



    def constant_int(self):
        num = ['0','1','2','3','4','5','6','7','8','9']

        if self.proxToken.nome in num:
            self.proxToken = self.lex.prox_token()

            while self.proxToken in num:
                self.proxToken = self.lex.prox_token()

        else:
            self.trata_erro(str(num))


    def constant_float(self):
        self.procedimento('constant_int')

        if self.proxToken.nome == '.':
            self.proxToken = self.lex.prox_token()

            self.procedimento('constant_int')

            if self.proxToken.nome == 'E':
                self.proxToken = self.lex.prox_token()

                if self.proxToken.nome in ['+', '-']:
                    self.proxToken = self.lex.prox_token()

                self.procedimento('constant_int')

        else:
            self.trata_erro('.')



    def trata_erro(self):
        pass

    
    def trata_erro(self, tokens):
        raise Exception(f'Erro: {tokens} esperado(s) ({str(self.proxToken)} encontrado)')
            

