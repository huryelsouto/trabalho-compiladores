from AnalisadorLexico import AnalisadorLexico


def main():
    lista_tokens = AnalisadorLexico.run('diagrama.json', 'programa.txt')

    print(lista_tokens)

main()