from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico
from Gramatica import Gramatica
from diagram_api.graphviz_fsa_to_diagram import graphviz_fsa_to_diagram

# graphviz_fsa_to_diagram('diagram_api/graphviz_fsa.txt')
G = Gramatica.from_json('gramatica.json')

sintatico = AnalisadorSintatico('diagram_api/diagrama_final.json', 'while.txt', G)

# print(sintatico.gramatica)

sintatico.drsr()

print(sintatico.lex.tabela_simbolos)