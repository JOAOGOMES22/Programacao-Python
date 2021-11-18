from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def login():
    if window.usuario.text() == 'admin' and window.senha.text() == 'admin':
        logado.show()
    else:
        QMessageBox.about(window, "Atenção!", "Usuário e/ou senha invalidos.\nTente novamente")


def cadastro():
    cadastrar.show()


def cadastrado():
    QMessageBox.about(cadastrar, "Cadastro realizado", "CADASTRADO COM SUCESSO!")


app = QtWidgets.QApplication([])
window = uic.loadUi("login.ui")
logado = uic.loadUi("logado.ui")
cadastrar = uic.loadUi("cadastro.ui")
window.logar.clicked.connect(login)
window.cadastro.clicked.connect(cadastro)
cadastrar.cadastrar.clicked.connect(cadastrado)
window.show()
app.exec()
