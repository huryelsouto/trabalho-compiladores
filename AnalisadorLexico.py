import Token,Automato

class AnalisadorLexico(object):


    def __init__(self, dir_automato, dir_arq):
        self.automato = Automato(dir_automato)
        self.dir_arq = self.dir_arq
        self.arq = None
        self.eof = False
        self.pos = 0


    # retorna lista de tokens do programa
    def run(self):
        tokens = []
        token = self.__run__(self.dir_arq)

        while not self.eof and token is not None:
            tokens.append(token)
            token = self.__run__(self.dir_arq)

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
            c = self.arq.read(1)
            self.pos += 1

            while not self.automato.final(s) and not s is None:
                s = self.automato.move(s, c)
                c = self.arq.read(1)
                self.pos += 1

            self.arq.close()

            if self.automato.final(s):
                return Token(self.automato.finais[s][0], self.automato.finais[s][1])
            else:
                return None

        except EOFError:
            self.arq.close()
            self.eof = True
            if self.automato.final(s):
                return Token(self.automato.finais[s][0], self.automato.finais[s][1])
            else:
                return None

            
