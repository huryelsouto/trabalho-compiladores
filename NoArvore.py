class NoArvore(object):

    def __init__(self, valor):
        self.valor = valor
        self.children = []

    def adiciona_filho(self, arv_filho):
        self.children.append(arv_filho)