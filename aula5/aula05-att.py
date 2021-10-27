NNote=int(input("Quantas notas voce ira cadastrar? "))
CTnota=[]
print("************************************")
for CT in range (1, NNote + 1):
    Nome= input('Nome do aluno(a): ')
    nota= int(input('Nota do aluno(a): '))
    print("************************************")
    CTnota.append([Nome,nota])

print("Escola Xuarnes - Rua dos Bobos nº0")
print("Notas dos alunos turma 3° ano A.\n")

for I in CTnota:
    print("-- Aluno(a): %6s -- Nota: %2d --" % (I[0], I[1]))

print("\n************************************")
print("Todos os alunos receberam suas notas!")