from PyQt5 import uic, QtWidgets
import mysql.connector

banco= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '1234',
    database= 'Python'
)

def cadastro():
    nome= janela.nome.text()
    email= janela.email.text()
    cursor= banco.cursor()
    sql= "INSERT INTO CadastroAluno (nome,email) VALUES (%s,%s)"
    colunas= (str(nome), str(email))
    cursor.execute(sql,colunas)
    banco.commit()

    msg= QMessageBox
    QMessageBox.about(janela,"Dados Salvos", "Seus dados foram salvos com sucesso!")
