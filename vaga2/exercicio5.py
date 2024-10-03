'''
#1ª versão -> inverte a frase inteira
def reverte_string(string):
    string_reversa = ''
    i = len(string) - 1
    for letra in string:
        string_reversa += string[i]
        i -= 1
    print(string_reversa)

string = input('Qual frase deseja reverter?\n')
reverte_string(string)
'''

#2ª versão -> mantém a ordem das palavras da frase e inverte cada palavra
def reverte_string(string):
    strings = string.split(' ')
    string_reversa = ''
    strings_reversas = []
    for pequena_string in strings:
        i = len(pequena_string) - 1
        for letra in pequena_string:
            string_reversa += pequena_string[i]
            i -= 1
            if i == -1:
                string_reversa += ' '
        strings_reversas.append(string_reversa)

    string_reversa.join(strings_reversas)
    print(string_reversa)

string = input('Qual frase deseja reverter?\n')
reverte_string(string)