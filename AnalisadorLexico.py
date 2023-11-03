from Token import Token
from Automato import Automato

class AnalisadorLexico(object):


    def __init__(self, dir_automato, dir_arq):
        self.automato = Automato(dir_automato)
        self.dir_arq = dir_arq
        self.arq = None
        self.eof = False
        self.pos = 0
        self.linha = 0
        self.coluna = 0


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
            stringLida = ''
            colunaCount = 0
            linhaCount = 0
            while not self.automato.final(s) and s is not None:
                if not self.automato.final(s) and s is not None:
                    character = self.arq.read(1)
                    s = self.automato.move(s, character)
                    stringLida += character
                    colunaCount += 1
                    
                    
                # print('\'' + character + '\' ' + str(s) + ' ' + str(self.pos))
                self.pos += 1

            self.arq.close()

            # print(self.automato.est_finais)
            if self.automato.final(s):
                
                if s in self.automato.est_lookaheads:
                    # print('lookaheads')
                    self.pos -= 1
                    colunaCount -= 1
                    stringLida = stringLida[0:-1]
                
                oldCol = 0
                for ch in stringLida:
                    if ch == '\n':
                        oldCol = self.coluna
                        linhaCount += 1
                        self.coluna = colunaCount-1
                        colunaCount = 0
                        
                print('Lexema: \'' + stringLida + '\'')
                print('Self.coluna: ' + (str(self.coluna) if colunaCount != 0 else str(oldCol)))
                print('Self.linha: ' + str(self.linha))
                print(Token(self.automato.est_finais[s][0], self.automato.est_finais[s][1]))
                print()

                self.coluna += colunaCount
                self.linha += linhaCount
                

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

            
