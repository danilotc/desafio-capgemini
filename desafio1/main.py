def cria_escada(numero=6):
    '''Recebe um número inteiro e monta uma escada com asterisco (*).'''
    for coluna in range(0, numero):
        for linha in range(0, numero):
            if coluna < linha:
                print(" ", end="")
        print("*" * (coluna + 1))


if __name__ == '__main__':
    # Se o parâmetro não for passado, montará uma escada de 6x6.
    cria_escada()
