from Gramatica import Gramatica
from TabelaDeSimbolos import TabelaDeSimbolos
from AnalisadorLexico import AnalisadorLexico
from diagram_api.graphviz_fsa_to_diagram import graphviz_fsa_to_diagram

graphviz_fsa_to_diagram('diagram_api/graphviz_fsa.txt')
tabela_simbolos = TabelaDeSimbolos()
lex = AnalisadorLexico("diagram_api/diagrama_final.json", "while.txt", tabela_simbolos)

tokens = lex.run()
print(tabela_simbolos)

# #G = Gramatica(V, T, P, S)
# G = Gramatica.from_json("gramatica.json")

# #pApc = G.__encontra_pApc__()
# #print(G.__pApcl__(pApc))

# print(G)

# # for token in tokens:
# #     print(token)

# #G.fatorar_gramatica()

# for v in G.V:
#     print(f"FIRST({v})={G.first(v)}")

# #print("\n----------------\n")

# for v in G.V:
#     print(f"FOLLOW({v})={G.follow(v)}")
