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
        if self.eof:
            return None

        self.arq = open(self.dir_arq, 'r')
        self.arq.seek(self.pos)
        
        s = self.automato.est_inicial
        
        try:
            old_char = ''
            
            while not self.automato.final(s) and s is not None:
                if not self.automato.final(s) and s is not None:
                    character = self.arq.read(1)
                    s = self.automato.move(s, character)
                print('\'' + character + '\' ' + str(s) + ' ' + str(self.pos))
                self.pos += 1

            self.arq.close()

            # print(self.automato.est_finais)
            if self.automato.final(s):
                if s in self.automato.est_lookaheads:
                    print('lookaheads')
                    self.pos -= 1
                
                print(Token(self.automato.est_finais[s][0], self.automato.est_finais[s][1]))
                return Token(self.automato.est_finais[s][0], self.automato.est_finais[s][1])
            else:
                return None

        except EOFError:
            self.arq.close()
            self.eof = True
            if self.automato.final(s):
                return Token(self.automato.est_finais[s][0], self.automato.est_finais[s][1])
            else:
                return None

            
