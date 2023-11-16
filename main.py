from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico
from Gramatica import Gramatica

G = Gramatica.from_json('gramatica.json')

sintatico = AnalisadorSintatico('diagram_api/diagrama_final.json', 'programa.txt', G)

print(sintatico.gramatica)

sintatico.drsr()

print(sintatico.lex.tabela_simbolos)