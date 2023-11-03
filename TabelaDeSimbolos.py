from Token import Token

class LinhaTabelaSimbolos(object):

    def __init__(self, token, lexema, valor, tipo_dado):
        self.token = token
        self.lexema = lexema 
        self.valor = valor 
        self.tipo_dado = tipo_dado

    def __str__(self):
        return '|' + str(self.token) + '\t\t\t|' + self.lexema + '\t\t\t|' + self.valor + '\t\t\t|' + self.tipo_dado

class TabelaDeSimbolos(object):

    def __init__(self):
        self.linhas = []

    def __str__(self):
        stringTable = '|' + 'TOKEN' + '\t\t\t|' + 'LEXEMA' + '\t\t\t|' + 'VALOR' + '\t\t\t|' + 'TIPO DO DADO\n'
        for linha in self.linhas:
            stringTable += (str(linha) + '\n')
        return stringTable