from Token import Token

class LinhaTabelaSimbolos(object):

    def __init__(self, token, lexema, valor, tipo_token, tipo_dado, linha, coluna):
        self.token = token
        self.lexema = lexema 
        self.valor = valor 
        self.tipo_token = tipo_token
        self.tipo_dado = tipo_dado
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return '|' + str(self.token) + (' ' * (20 - len(str(self.token)))) +'|' + str(self.lexema) + (' ' * (20 - len(str(self.lexema)))) + '|' + str(self.valor) + (' ' * (20 - len(str(self.valor)))) +'|' + str(self.tipo_token) +  (' ' * (20 - len(str(self.tipo_token)))) + '|' + str(self.tipo_dado) + (' ' * (20 - len(str(self.tipo_dado)))) + '|' + str(self.linha) + (' ' * (20 - len(str(self.linha)))) + '|' + str(self.coluna)

class TabelaDeSimbolos(object):

    def __init__(self):
        self.linhas = []

    def __str__(self):
        stringTable = '|' + 'TOKEN' + (' ' * (20 - len('TOKEN'))) +'|' + 'LEXEMA' + (' ' * (20 - len('LEXEMA'))) + '|' + 'VALOR' + (' ' * (20 - len('VALOR'))) +'|' + 'TIPO DO TOKEN' +  (' ' * (20 - len('TIPO DO TOKEN'))) + '|' + 'TIPO DO DADO' + (' ' * (20 - len('TIPO DO DADO'))) + '|' + 'LINHA' + (' ' * (20 - len('LINHA'))) + '|' + 'COLUNA\n'
        for linha in self.linhas:
            stringTable += (str(linha) + '\n')
        return stringTable
    
    def adiciona_linha(self, token):
        if token not in self.tabela:
            self.tabela.append(token)

    def prox_linha(self):
        return len(self.linhas)