SenhaU1= '1234'
ct= 0

login=input('Digite seu usuario: \n')
senha=input('Digite sua senha: \n')

if senha != SenhaU1:
    for ct in range(2):
        senha=input('Senha invalida, digite novamente: \n')
       
        if senha == SenhaU1:
            print('Acesso liberado')
            break
else:
    print('Acesso liberado!')

if senha != SenhaU1:
    print('Acesso bloqueado!')
    



