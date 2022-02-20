import re


def valida_senha(string):
    '''Verifica regras antes de gerar uma senha forte.'''

    # Variáveis utilizadas
    numero = 0
    maiusculo = 0
    minusculo = 0
    especial = 0

    # Verificar existência de números, sai do
    # loop se encontrar pelo menos 1
    for digito in range(0, len(string)):
        if string[digito].isnumeric():
            numero += 1
            break

    # Verifica existência de letra em maiúsculo,
    # sai do loop se encontrar pelo menos 1
    for digito in range(0, len(string)):
        if string[digito].isupper():
            maiusculo += 1
            break

    # Verifica existência de letra em minúsculo,
    # sai do loop se encontrar pelo menos 1
    for digito in range(0, len(string)):
        if string[digito].islower():
            minusculo += 1
            break

    # Verifica existência de caracter especial
    simbolos = re.compile("[!@#$%^&*()-+]")
    if bool(simbolos.search(string)):
        especial = 1

    # Verifica se o mínimo de 6 caracteres está sendo atendido
    if len(string) < 6:
        forte = 6
        fraca = len(string)
        falta = forte - fraca

        # Informa quantos caracteres faltam e quais são obrigatórios
        print(f"\nFalta {falta} caractere(s) para atingir o mínimo necessário")
        if numero == 0:
            print("Pelo menos 1 número.")
        if maiusculo == 0:
            print("Pelo menos 1 letra em maiúsculo.")
        if minusculo == 0:
            print("Pelo menos 1 letra em maiúsculo.")
        if especial == 0:
            print("Pelo menos 1 caractere especial.")
        print() # para gerar uma linha
    else:
        if (numero == 0) or (maiusculo == 0) or (minusculo == 0) or (especial == 0):
            print("\nAdicione os seguintes caracteres antes de continuar:")
            if numero == 0:
                print("Pelo menos 1 número.")
            if maiusculo == 0:
                print("Pelo menos 1 caracter em maiúsculo.")
            if minusculo == 0:
                print("Pelo menos 1 caracter em minúsculo.")
            if especial == 0:
                print("Pelo menos 1 caracter especial.")
            print() # para gerar uma linha
        else:
            return True
