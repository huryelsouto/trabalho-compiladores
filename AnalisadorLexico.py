import Token,Automato

class AnalisadorLexico(object):

    @staticmethod
    def run(dir_automato, dir_programa):
        automato = Automato(dir_automato)
        arq = open(dir_programa, 'r')
        s = automato.est_inicial


        try:
            c = arq.read(1)

            while not automato.final(s) and not s is None:
                s = automato.move(s, c)
                c = arq.read(1)

        except EOFError:
            if automato.final(s):
                return Token(automato.finais[s][0], automato.finais[s][1])
            
