'''
Nunca tinha ouvido falar em anagrama, tentei estudar, mas não encontrei
material com explicações que sejam claras e didáticas. Tentei fazer de
diversas formas, ainda assim não consegui.

O script abaixo será atualizado quando eu aprender e entender de forma
definitiva como funciona a lógica dessa questão. Help me?
'''


def tentativa_anagrama(texto):
    lista=[]
    for i in range(0, len(texto)):
        # print(i)

        if i==0:
            var1=texto[i]

            for j in range(0, len(texto)):
                # print('--', j)
                
                if var1==texto[j]:
                    # print('-----', texto[j])
                    lista.append(texto[j])
        
        if i==1:
            var2=texto[:2]
            
            if var2 in texto:
                # print('--', var2)
                lista.append(var2)
        
        if i==3:
            var3=texto[:3]

            if var3 in texto:
                print('--', var3)
                
    return lista


if __name__ == '__main__':
    print(tentativa_anagrama('ovo'))
