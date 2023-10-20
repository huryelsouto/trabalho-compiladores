from AnalisadorLexico import AnalisadorLexico
from Gramatica import Gramatica

class AnalisadorSintatico():


    def __init__(self, dir_automato, dir_programa, gramatica):
        self.lex = AnalisadorLexico(dir_automato, dir_programa)
        self.gramatica = gramatica
        



    # Descida Recursiva sem Retrocesso
    def drsr(gramatica, sintatico):
        proxToken = 