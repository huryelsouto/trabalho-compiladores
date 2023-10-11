class Token(object):

    def __init__(self, nome, atributo):
        self.nome = nome
        self.atributo = atributo

    def __str__(self):
        return "<" + self.nome + "," + self.atributo + ">"
    
    def __eq__(self, other):
        return self.nome == other.nome and self.atributo == other.atributo