###################################################################################
#  Atividade 01                                                                   # 
#  No primeiro IF identifico se esta dentro do limite de caracteres, no segundo   #
#  dentifico se as credenciais estão corretas.                                    #
###################################################################################

print('!Digite seu login e senha!.\n')

Log=input('Login: \n')
Sen=input('Senha: \n')

if len(Log) <= 6 and len(Sen) <= 6 : 
    if Log == 'Senac' and Sen == '2021' :
        print('Acesso liberado!')
    else:
        print('Usuario ou senha invalidos')
else:
    print('Usuario ou senha ultrapassaram os limites de caracteres!')
