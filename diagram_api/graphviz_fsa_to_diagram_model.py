# Nome do arquivo de origem e destino
import re

def convert_graphviz_fsa_to_driagram_model(arquivo_origem):
    # Abra o arquivo de origem para leitura
    with open(arquivo_origem, 'r') as arquivo_origem:
        linhas = arquivo_origem.readlines()

    linhas_transicoes = []
    estados_finais = set()
    simbolos = set()
    nfa = {}
    aux_infos = {}

    for linha in linhas:
        # Remova espaços em branco em excesso e verifique se a linha não está vazia
        linha_processada = linha.strip()
        linha_processada = linha_processada.replace(" ", "")

        padrao_estados = r'([^-]+)->([^\[]+)'
        padrao_simbolo = r'label="([^\]]+)"]'
        padrao_estado_final = r'doublecircle];([^;]+)'
        

        # Use re.search() para encontrar o padrão na expressão
        correspondencia_estados = re.search(padrao_estados, linha_processada)
        correspondencia_symbolos = re.search(padrao_simbolo, linha_processada)
        correspondencia_estados_finais = re.search(padrao_estado_final, linha)
        
        if correspondencia_estados and correspondencia_symbolos:
            est_origem = str(correspondencia_estados.group(1))
            est_destino = str(correspondencia_estados.group(2))
            simb = str(correspondencia_symbolos.group(1))

            if est_origem == est_destino and est_origem in estados_finais:
                if simb != '*':
                    padrao_return = r'return\(([^"]+)\)'
                    correspondencia_return = re.search(padrao_return, simb)
                    if correspondencia_return:
                        if(est_origem in aux_infos):
                            aux_infos[est_origem]['return'] = str(correspondencia_return.group(1))
                        else:
                            aux_infos[est_origem] = {'return': str(correspondencia_return.group(1))}
                else:
                    if(est_origem in aux_infos):
                        aux_infos[est_origem]['lookahead'] = ['yes']
                    else:
                        aux_infos[est_origem] = {'lookahead': ['yes']}
            else:
                simbolos.add(simb)
                if(est_origem in nfa):
                    if(simb in nfa[est_origem]):
                        nfa[est_origem][simb].extend([est_destino])
                    else:
                        nfa[est_origem][simb] = [est_destino]
                else:
                    nfa[est_origem] = {simb:[est_destino]}

        if correspondencia_estados_finais:
            est_fin = str(correspondencia_estados_finais.group(1))
            est_fin = est_fin.strip()
            est_fin = est_fin.split(' ')
                    
            for est in est_fin:
                estados_finais.add(est)


        
    for est in estados_finais:
        if est in nfa.keys():
            nfa[str(est)]['state'] = ['final']
        else:
            nfa[str(est)] = {'state':['final']}

    for est in nfa.keys():
        if est in estados_finais:
            nfa[str(est)]['state'] = ['final']
        else:
            nfa[str(est)]['state'] = ['normal']

        for simb in simbolos:
            if simb not in nfa[str(est)]:
                nfa[str(est)][simb] = []

        
    return nfa, aux_infos




