import json
from justNfa2Dfa import JustNfa2Dfa
from automato_site_to_convert_json import convert_automato_site_to_our_model
def afnd_site_to_afd(dir):

    nfa, aux_infos = convert_automato_site_to_our_model(dir)
    nfa['0']['state'] = ['start']

    # print(nfa)
    # print(aux_infos)

    nfa = json.dumps(nfa)
    obj = JustNfa2Dfa(nfa)

    return(obj, aux_infos)

def afd_to_json():
    obj, aux_infos = afnd_site_to_afd('afnd_afd_api/automato-site.txt')
    
    afd = obj.dfa
    mapFinais = obj.mapFinal
    
    inicial = ''
    transicoes = []
    finais = {}
    look_aheads = set()
    
    for est_origem in afd.keys():
        for simb in afd[est_origem].keys():
            if simb != 'state': # transicoes
                for est_dest in afd[est_origem][simb]:
                    transicoes.append([est_origem, est_dest, simb])
            elif simb == 'state': 
                if afd[est_origem][simb] == ['start']: # estado inicial
                    inicial = est_origem
                elif afd[est_origem][simb] == ['final']: # estados finais
                    for antigo_estado_fin in mapFinais.keys():
                        if antigo_estado_fin in aux_infos.keys():
                            if 'return' in aux_infos[antigo_estado_fin]:
                                finais[mapFinais[antigo_estado_fin]] = aux_infos[antigo_estado_fin]['return'].split(',')
                            if 'lookahead' in aux_infos[antigo_estado_fin]:
                                look_aheads.add(mapFinais[antigo_estado_fin])

    # print('\n\n')
    # #print(inicial)
    # print()
    # #print(finais)
    # print()
    # print(transicoes)
    # print()
    # #print(list(look_aheads))

    d = dict()

    a = open("diagrama.json", 'r')
    a = json.load(a)

    d.update({"definicoes_regulares": a['definicoes_regulares'],
              "inicial": inicial,
              "finais": finais,
              "transicoes": transicoes,
              "lookaheads": list(look_aheads)})

    # print(d)

    d = json.dumps(d)

    with open("afnd_afd_api/diagrama_final.json", "w") as f:
        f.write(d)

    

afd_to_json()

# nfa = {
    #     '0':{'a': [], 'b': [],'λ': ['1', '7'], 'state': ['start']},
    #     '1':{'a': [], 'b': [],'λ': ['2', '4'], 'state': ['normal']},
    #     '2':{'a': ['3'], 'b': [],'λ': [], 'state': ['normal']},
    #     '3':{'a': [], 'b': [],'λ': ['6'], 'state': ['normal']},
    #     '4':{'a': [], 'b': ['5'],'λ': [], 'state': ['normal']},
    #     '5':{'a': [], 'b': [],'λ': ['6'], 'state': ['normal']},
    #     '6':{'a': [], 'b': [],'λ': ['1','7'], 'state': ['normal']},
    #     '7':{'a': ['8'], 'b': [],'λ': [], 'state': ['normal']},
    #     '8':{'a': [], 'b': ['9'],'λ': [], 'state': ['normal']},
    #     '9':{'a': [], 'b': ['10'],'λ': [], 'state': ['normal']},
    #     '10':{'a': [], 'b': [],'λ': [], 'state': ['final']}
    # }
    
    # Estado    a   b
    # A         B   C
    # B         B   D
    # C         B   C
    # D         B   E
    # E         B   C

    # Estado    a   b
    # 0         1   2
    # 1         1   3
    # 2         1   2
    # 3         1   4
    # 4         1   2