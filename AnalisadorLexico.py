from Token import Token
from Automato import Automato
from TabelaDeSimbolos import LinhaTabelaSimbolos,TabelaDeSimbolos
import copy

class AnalisadorLexico(object):


    def __init__(self, dir_automato, dir_arq, tabela_simbolos=TabelaDeSimbolos()):
        self.automato = Automato(dir_automato)
        self.dir_arq = dir_arq
        self.tabela_simbolos = tabela_simbolos

        self.arq = None
        self.eof = False
        self.pos = 0
        self.linha = 0
        self.coluna = 0


    # retorna lista de tokens do programa
    def run(self):
        tokens = []
        token = self.prox_token()

        while not self.eof and token is not None:
            tokens.append(token)
            token = self.prox_token()
            # print(token)

        return tokens
    
    # devolve o próximo token ignorando WS e COMMENTS
    def prox_token(self):
        linhaTabelaSimb = self.__prox_token__aux__()

        if linhaTabelaSimb is not None:
            if (linhaTabelaSimb.token.nome == 'WS' or linhaTabelaSimb.token.nome == 'COMMENT'):
                while linhaTabelaSimb.token is not None and (linhaTabelaSimb.token.nome == 'WS' or linhaTabelaSimb.token.nome == 'COMMENT'):
                    linhaTabelaSimb = self.__prox_token__aux__()

            self.tabela_simbolos.linhas.append(linhaTabelaSimb)
            return linhaTabelaSimb.token
        
        return None

    # le um token soh (retorna Token, ou None caso erro)
    # atualiza self.eof para True caso chegue no EOF do arq
    # considera WS e COMMENT como tokens tambem
    def __prox_token__aux__(self):
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
                        
                

                lexema = stringLida
                # print(self.automato.est_finais[s])
                att = 'NULL' if self.automato.est_finais[s][1] == '' else self.automato.est_finais[s][1]
                token = Token(self.automato.est_finais[s][0], att)
                linha = self.linha
                coluna = self.coluna if colunaCount != 0 else oldCol

                tipo_token = token.nome
                valor_token = self.tabela_simbolos.prox_linha()
                tipo_dado = None

                
                # print('Lexema: \'' + lexema + '\'')
                # print('Self.coluna: ' + str(coluna))
                # print('Self.linha: ' + str(linha))
                # print(token)
                # print()

                self.coluna += colunaCount
                self.linha += linhaCount
                

                return LinhaTabelaSimbolos(token, lexema, valor_token, tipo_token, tipo_dado, linha, coluna)
            else:
                return None
                # raise ValueError(f'Error: erro pertencente à linha \'{self.linha}\' e à coluna \'{self.coluna}\'')

        except EOFError:
            self.arq.close()
            self.eof = True
            if self.automato.final(s):
                return LinhaTabelaSimbolos(token, lexema, valor_token, tipo_token, tipo_dado, linha, coluna)
            else:
                return None
                # raise ValueError(f'Error: erro no lexema \'{lexema}\' pertencente à linha \'{self.linha}\' e à coluna \'{self.coluna}\'')


    def rollback(self, pos):
        if pos < self.pos and pos >= 0:
            self.pos = copy.deepcopy(pos)


    def get_pos(self):
        return copy.deepcopy(self.pos)