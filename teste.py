from Gramatica import Gramatica
from TabelaDeSimbolos import TabelaDeSimbolos
from AnalisadorLexico import AnalisadorLexico
from diagram_api.graphviz_fsa_to_diagram import graphviz_fsa_to_diagram

graphviz_fsa_to_diagram('diagram_api/graphviz_fsa.txt')
tabela_simbolos = TabelaDeSimbolos()
lex = AnalisadorLexico("diagram_api/diagrama_final.json", "triangulo.txt", tabela_simbolos)

tokens = lex.run()


# for token in tokens:
#     print(token)

print(tabela_simbolos)

# V = ["E", "E\'", "T", "T\'", "F"]
# T = ["+", "", "*", "(", ")", "id"]
# P = [["E", "T E\'"], ["E\'", "+ T E\'"], ["E\'", ""],
#      ["T", "F T\'"], ["T\'", "* F T\'"], ["T\'", ""],
#      ["F", "( E )"], ["F","id"]]
# S = "E"

# G = Gramatica(V, T, P, S)
# #G = Gramatica.from_json("gramatica.json")

# pApc = G.__encontra_pApc__()
# print(G.__pApcl__(pApc))

# print("\n----------------\n")

# G.fatorar_gramatica()

#for v in G.V:
#    print(f"FIRST({v})={G.first(v)}")

#print("\n----------------\n")

#for v in G.V:
#    print(f"FOLLOW({v})={G.follow(v)}")
