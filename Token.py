class Token(object):

    def __init__(self, nome, atributo):
        self.nome = nome
        self.atributo = atributo


    @staticmethod
    def __str_tokens__(tokens):
        l = '['

        for token in tokens:
            l += str(token) + ', '

        l = l[:-2]
        l += ']'

        return l

    def __str__(self):
        return "<" + self.nome + "," + self.atributo + ">"
    
    def __eq__(self, other):
        return self.nome == other.nome and self.atributo == other.atributo