###################################################################################
# Atividade 03                                                                    #
# Primeiro solicito dois valore e logo em seguida vejo se os valores passados são #
# numericos, se for verdade passo para a segunda verificação, se for falso aviso  #
# que os valores nao foram identificados.                                         #
# Na segunda verificação identifico se a soma de caracteres passa de 10, se nao   #
# passar informo a soma, se passar aviso na tela que passou o numero de caracteres#
###################################################################################

print('Identificando numeros!\n\n')

n1=input('Digite um valor inteiro\n')
n2=input('Digite mais um valor inteiro\n')

if n1.isnumeric() and n2.isnumeric():
    X= len(n1) + len(n2)
    
    if X <= 10:
        print(f'\nA soma dos caracteres é: {X}\n')
    else:
        print('\nUltrapassou o numero de caracteres perminitido!\n')
else:
    print('\nValor não identificado!\n')