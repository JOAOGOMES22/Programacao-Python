from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import Jogo_1_Snake
import Jogo_2_Shooter



banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cobrinha'
)


def log():
    principal.close()
    login.show()

def pg_cad():
    principal.close()
    cadastro.show()

def logar():
    usuario = login.lineLog.text()
    senha = login.linePass.text()
    sql = "select senha_player from jogadores where usuario_player = '{}'".format(usuario)
    conexao = banco.cursor()
    conexao.execute(sql)
    senha_db = conexao.fetchall()
    if senha == senha_db[0][0]:
        login.close()
        game.show()
    else:
        QMessageBox.about(login, 'Erro', 'Usuario e/ou senha incorretos!')

def voltar():
    login.close()
    principal.show()
    
def voltar2():
    cadastro.close()
    principal.show()

def jogo1():
    Jogo_1_Snake.Snake()

def jogo2():
    Jogo_2_Shooter.App()

def cadastro_jogador():
    
    nome = cadastro.LineName.text()
    email = cadastro.LineEm.text()
    usuario = cadastro.LineUse.text()
    senha = cadastro.LinePas.text()
    senha2 = cadastro.LinePas2.text()

    if senha != senha2: 
         QMessageBox.about(cadastro, "Atenção!", "senhas não compativeis.")
        
    sexo = ''
    if cadastro.SexM.isChecked():
        sexo = 'Masculino'
    elif cadastro.SexF.isChecked(): 
        sexo = 'Feminino'
    elif cadastro.SexNF.isChecked():
        sexo = 'Nao Informado'

    cursor = banco.cursor() 
    sql= "INSERT INTO jogadores(nome_player, email_player, usuario_player, senha_player, genero_player)" "VALUES(%s,%s,%s,%s,%s)"
    colunas = (str(nome), str(email), str(usuario), str(senha), sexo)
    cursor.execute(sql, colunas)
    banco.commit()

    #QMessageBox.about(cadastro, "Sucesso!", "Cadastrado com sucesso")

    cadastro.LineName.setText('')
    cadastro.LineEm.setText('')
    cadastro.LineUse.setText('')
    cadastro.LinePas.setText('')
    cadastro.LinePas2.setText('')
    


app = QtWidgets.QApplication([])
principal = uic.loadUi("PGPrincipal.ui")
cadastro = uic.loadUi("PGcad.ui")
login = uic.loadUi("PGLog.ui")
game = uic.loadUi("PGGame.ui")
principal.BTcad.clicked.connect(pg_cad)
principal.BTlog.clicked.connect(log)
cadastro.BTCad1.clicked.connect(cadastro_jogador)
cadastro.BTBack.clicked.connect(voltar2)
login.BTlog1.clicked.connect(logar)
login.BTback.clicked.connect(voltar)
game.jogo1.clicked.connect(Jogo_1_Snake.Snake)
game.jogo2.clicked.connect(Jogo_2_Shooter.App)


principal.show()
app.exec()