class TabelaSimbolo(object):

    
    def __init__(self):
        self.tabela = []

    
    def adiciona_token(self, token):
        if token not in self.tabela:
            self.tabela.append(token)

    