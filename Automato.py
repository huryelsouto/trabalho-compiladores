import json

class Automato(object):


    def __init__(self, dir):
        f = open(dir)
        diagrama = json.load(f)

        self.alfabeto = set(map(lambda elem: elem if diagrama['transicoes'][2] not in diagrama['definicoes_regulares'].keys() else diagrama['definicoes_regulares'][elem], diagrama['transicoes']))
        self.estados = set(map(lambda elem: elem[0], diagrama['transicoes']))
        self.transicoes = set(map(lambda est, prox_est, simb: (est, prox_est, simb if simb not in diagrama['definicoes_regulares'].keys() else diagrama['definicoes_regulares'][simb]), diagrama['transicoes']))
        self.est_inicial = diagrama['inicial']
        self.est_finais = diagrama['finais']


    def move(self, est_atual, simbolo_lido):
        for (est_a, est_prox, simb_lido) in self.transicoes:
            if (est_atual, simbolo_lido) == (est_a, simb_lido):
                return est_prox
        return None # estado de erro == None
    
    def final(self, estado):
        return estado in self.est_finais