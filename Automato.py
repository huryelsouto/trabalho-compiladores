import json

class Automato(object):


    def __init__(self, dir):
        f = open(dir)
        diagrama = json.load(f)

        # print(diagrama['transicoes'])
        
        self.alfabeto = set(map(lambda elem: elem[2] if elem[2] not in diagrama['definicoes_regulares'].keys() else diagrama['definicoes_regulares'][elem[2]], diagrama['transicoes']))
        self.estados = set(map(lambda elem: str(elem[0]), diagrama['transicoes']))
        self.transicoes = set(map(lambda elem: ((str(elem[0]), str(elem[1]), elem[2]) if elem[2] not in diagrama['definicoes_regulares'].keys() else (str(elem[0]), str(elem[1]),diagrama['definicoes_regulares'][elem[2]])), diagrama['transicoes']))
        self.est_inicial = str(diagrama['inicial'])
        self.est_finais = diagrama['finais']
        self.est_lookaheads = diagrama['lookaheads']


    def move(self, est_atual, simbolo_lido):
        # print(est_atual + ' ' + '\'' + simbolo_lido + '\'')
        for (est_a, est_prox, simb_lido) in self.transicoes:
            if est_a == est_atual:
                # print(est_a + ' ' + est_prox + ' \'' + simb_lido + '\'')
                # print(est_atual + ' \'' + simbolo_lido + '\'')
                if (est_atual, simbolo_lido) == (est_a, simb_lido):
                    return est_prox
        return None # estado de erro == None
    
    def final(self, estado):
        # print(list(self.est_finais.keys()))
        return str(estado) in list(self.est_finais.keys())