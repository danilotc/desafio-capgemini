def cria_escada(n):
    '''Recebe um número inteiro e monta uma escada
    com a mesma proporção para base e altura'''

    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                print(" ", end="")
        print("*" * (i + 1))

if __name__ == '__main__':
    cria_escada(6)
