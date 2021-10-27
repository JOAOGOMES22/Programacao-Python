###################################################################################
# Atividade 02                                                                    #
# Para facilitar os testes utilizei X como variavel para definir a idade do coutn,#
# agora o usuario pode escolher a idade a ser contada                             #
###################################################################################
print('Idade dos alunos \n')

x=int(input('Qual idade vc quer identificar no sistema? \n\n'))

old=[18,19,20,20,16,19,14,18,20,18,18,18,18,18,18,18,18,19,19,20,17].count(x)

if x >= 18:
    print(f'\nTem {old} alunos com {x} anos cadastrado')
    if old == 10:
        print('\nCadastros realizados! \n')
    else:
        print(f'\nÉ prmitido realizar o cadastro de até 10 alunos com {x} anos! \n')
else:
    print('\n Idade invalida\n')
