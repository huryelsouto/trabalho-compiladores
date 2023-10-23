from Gramatica import Gramatica

V = ["E", "E\'", "T", "T\'", "F"]
T = ["+", "", "*", "(", ")", "id"]
P = [["E", "T E\'"], ["E\'", "+ T E\'"], ["E\'", ""],
     ["T", "F T\'"], ["T\'", "* F T\'"], ["T\'", ""],
     ["F", "( E )"], ["F","id"]]
S = "E"

G = Gramatica(V, T, P, S)

print(G)

print("\n----------------\n")

for v in G.V:
    print(f"FIRST({v})={G.first(v)}")

print("\n----------------\n")

for v in G.V:
    print(f"FOLLOW({v})={G.follow(v)}")
