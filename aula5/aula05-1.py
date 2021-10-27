prod=int(input("Digite quantos produtos deseja cadastrar: "))
venda=[]
print("------------------------------")
for CT in range (1, prod + 1):
    produto= input('Produto: ')
    qtd= int(input('Quantidade: '))
    preco= float(input('Preço: '))
    print("------------------------------")
    venda.append([produto, qtd, preco])

soma=0.00
print("Supermercado Xuarnes - Rua dos Penis")
print("Comprovantes de pagamento.\n")

for I in venda:
    print("%10s --> %d x R$%.2f = R$%.2f" % (I[0], I[1], I[2],I[1]*I[2]))

    soma += I[1]*I[2]

print("\n------------------------------")
print("O valor total da sua compra foi: R$%.2f " % soma)