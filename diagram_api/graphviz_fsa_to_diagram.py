import re
import json
from diagram_api.graphviz_fsa_to_diagram_model import convert_graphviz_fsa_to_driagram_model

def graphviz_fsa_to_diagram(dir):
    afd, aux_infos = convert_graphviz_fsa_to_driagram_model(dir)
    afd['0']['state'] = ['start']

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
                    if est_origem in aux_infos.keys() and 'return' in aux_infos[est_origem]:
                        finais[est_origem] = aux_infos[est_origem]['return'].split(',')
                    if est_origem in aux_infos.keys() and 'lookahead' in aux_infos[est_origem]:
                        look_aheads.add(est_origem)

    d = dict()

    a = open("diagram_api/definicoes_regulares.json", 'r')
    a = json.load(a)

    d.update({"definicoes_regulares": a['definicoes_regulares'],
              "inicial": inicial,
              "finais": finais,
              "transicoes": transicoes,
              "lookaheads": list(look_aheads)})
    
    # print(d['transicoes'])
    # ['0', '69', 'acdfghjklmnoqsvxyzACDFGHJKLMNOQSVXYZ']
    # ['0', 'dig', 'digito']
    newTransicoes = []
    ascii_characters = ''.join([chr(i) for i in range(32, 127)])
    print(ascii_characters)

    for transicao in d['transicoes']: 

        if(len(transicao[2]) > 1):
            if transicao[2][0] != '^': # digito (CERTOOOO)
                stringChars = d['definicoes_regulares'][transicao[2]] if(transicao[2] in d['definicoes_regulares'].keys()) else transicao[2]
                for character in stringChars:
                        newTransicoes.append([transicao[0], transicao[1], character])
            else: 
                definicaoRegular = transicao[2][1:]
                
                if(len(definicaoRegular) == 1): # ^p (CERTOOOO)
                    str_form = f'[^{definicaoRegular}]'
                    try:
                        ascii_characters_exc = re.findall(str_form, ascii_characters)
                    except:
                        print('AAAAAAA')
                        str_form = f'[^\{definicaoRegular}]'
                        ascii_characters_exc = re.findall(str_form, ascii_characters)
                        # print(str_form)
                        # print(ascii_characters)

                    for character in ascii_characters_exc:               
                        newTransicoes.append([transicao[0], transicao[1], character])
                else: # ^digito , ^digito_ 
                    ascii_intersection = ''.join([chr(i) for i in range(32, 127)])

                    for definicao in d['definicoes_regulares'].keys(): # digitoletra
                        padrao_def = definicao
                        correspondencia_def = re.search(padrao_def, definicaoRegular)
                        
                        if correspondencia_def:
                            for character in ascii_intersection:
                                if character not in d['definicoes_regulares'][definicao]:
                                    ascii_intersection.replace(character, '')
                            
                            definicaoRegular = re.findall(definicao, definicaoRegular)
                            definicaoRegular = ''.join(definicaoRegular)
                    
                    str_form = f'[^{definicaoRegular}]' # sobra _ em digito_
                    try:
                        ascii_characters_exc = re.findall(str_form, ascii_intersection)
                    except:
                        str_form = f'[^\{definicaoRegular}]'
                        ascii_characters_exc = re.findall(str_form, ascii_intersection)
                        
                    for character in ascii_characters_exc:               
                        newTransicoes.append([transicao[0], transicao[1], character])
                    
        else: # p CERTOOOO
            newTransicoes.append([transicao[0], transicao[1], transicao[2]])

        
        print(transicao)

    print('AAAAAAAA')
    for t in newTransicoes:
        if (t[0] == '103' and t[1] == '103'):
            print(t)
    # print(newTransicoes)
    d = json.dumps(d)



    with open("diagram_api/diagrama_final.json", "w") as f:
        f.write(d)

    

# afd = {
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