from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'curso'
)

def cadastro():
    matricula = janela.box1.text()
    nome = janela.box2.text()
    email = janela.box3.text()
    telefone = janela.box4.text()
    
    sexo = ''
    if janela.bt1.isChecked():
        sexo = 'M'
    elif janela.bt2.isChecked(): 
        sexo = 'F'
    elif janela.bt3.isChecked():
        sexo = 'NI'

    cursor = banco.cursor() 
    sql= "INSERT INTO cadastro_alunos(matricula_aluno, nome_aluno, email_aluno, telefone_aluno, sexo_aluno)" "VALUES(%s,%s,%s,%s,%s)"
    colunas = (str(matricula), str(nome), str(email), str(telefone), sexo)
    cursor.execute(sql, colunas)
    banco.commit()


app = QtWidgets.QApplication([])
janela = uic.loadUi("Cadastro_senac.ui")
janela.env1.clicked.connect(cadastro)

janela.show()
app.exec()