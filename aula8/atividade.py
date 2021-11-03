from itertools import zip_longest
print("===Cadastro de clientes===")

nome=['Josue','Paula','Ana','Stephani','Jhenyfer']
idade=[19,25,20,17,18]
cidade=['Curitiba','Ponta Grossa','Londrina','Curitiba','Florianopolis']
estado=['Parana','Parana','Parana','Parana','Santa Catarina']

cliente= zip_longest(nome,idade,cidade,estado)

print(list(cliente))