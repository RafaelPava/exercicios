def verifica_a(string):
    qtd_a = 0
    for a in string:
        if a == 'a' or a == 'A' or a == 'á' or a == 'Á' or a == 'à' or a == 'À':
            qtd_a += 1
    print(f'Quantidade de letras "a" na frase: {qtd_a}')

string = input('Qual é a frase que deseja contar a quantidade de letras a?\n')
verifica_a(string)