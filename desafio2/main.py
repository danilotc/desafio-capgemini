from senha_forte import valida_senha

senha = str(input("\nDigite sua senha [min 6 caracteres]: "))
caracter_adicionado = ""

while True:
    if valida_senha(senha):
        break
    else:
        cont = 0
        while len(senha) < 6:
            caracter_adicionado = str(input("Adicione os caracteres que faltam: "))
            senha += caracter_adicionado

# Apenas para verificar a junção das partes faltantes
print("OK! Tudo certo para gerar uma senha forte!\n")
print(f"Sua senha: {senha}\n")
