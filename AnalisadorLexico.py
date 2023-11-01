from Token import Token
from Automato import Automato

class AnalisadorLexico(object):


    def __init__(self, dir_automato, dir_arq):
        self.automato = Automato(dir_automato)
        self.dir_arq = dir_arq
        self.arq = None
        self.eof = False
        self.pos = 0


    # retorna lista de tokens do programa
    def run(self):
        tokens = []
        token = self.__run__()

        while not self.eof and token is not None:
            tokens.append(token)
            token = self.__run__()

        return tokens
            

    # le um token soh (retorna Token, ou None caso erro)
    # atualiza self.eof para True caso chegue no EOF do arq
    def __run__(self):
        # print('1')
        if self.eof:
            # print('2')
            return None

        self.arq = open(self.dir_arq, 'r')
        self.arq.seek(self.pos)
        
        s = self.automato.est_inicial
        state = s
        # print(self.automato.est_finais)
        # for est_i, est_d, simb_l in self.automato.transicoes:
        #     if est_i == '9' and simb_l == 'r':
        #         print(est_i + ' ' + est_d + ' ' + simb_l)

        try:
            # print('3')
            c = self.arq.read(1)
            self.pos += 1

            stringLida = c
            while not self.automato.final(s) and s is not None:
                state = s
                s = self.automato.move(s, c)
                if s is not None:
                    state = s
                c = self.arq.read(1)
                stringLida += c
                print(s)
                print(stringLida)

                self.pos += 1

            self.arq.close()
            # print(state)

            if self.automato.final(state):
                print('FINAL')
                return Token(self.automato.est_finais[state][0], self.automato.est_finais[s][1])
            else:
                return None

        except EOFError:
            self.arq.close()
            self.eof = True
            if self.automato.final(state):
                return Token(self.automato.est_finais[state][0], self.automato.est_finais[state][1])
            else:
                return None

            
