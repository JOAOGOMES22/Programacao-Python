from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from collections import deque, namedtuple
from random import randint
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import pyxel


banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cobrinha'
)

Point = namedtuple("Point", ["x", "y"])  # Convenience class for coordinates


#############
# Constants #
#############

COL_BACKGROUND = 2
COL_BODY = 11
COL_HEAD = 7
COL_DEATH = 8
COL_APPLE = 8

TEXT_DEATH = ["Fim de Jogo", "(Q)UIT", "(R)ESTART"]
COL_TEXT_DEATH = 0
HEIGHT_DEATH = 9

WIDTH = 50
HEIGHT = 70

HEIGHT_SCORE = pyxel.FONT_HEIGHT
COL_SCORE = 6
COL_SCORE_BACKGROUND = 5

UP = Point(0, -1)
DOWN = Point(0, 1)
RIGHT = Point(1, 0)
LEFT = Point(-1, 0)

START = Point(5, 5 + HEIGHT_SCORE)


###################
#O jogo em si#
###################


class Snake:
    """A classe que configura e executa o jogo."""

    def init(self):
        """Inicie o pyxel, configure as variáveis ​​iniciais do jogo e execute."""

        pyxel.init(WIDTH, HEIGHT, title="Snake!", fps=10, capture_scale=4)
        define_sound_and_music()
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        """Inicie variáveis-chave (direção, cobra, maçã, pontuação, etc.)"""

        self.direction = RIGHT
        self.snake = deque()
        self.snake.append(START)
        self.death = False
        self.score = 0
        self.generate_apple()

        pyxel.playm(0, loop=True)

    ##############
    # Lógica do Jogo #
    ##############

    def update(self):
        """Atualize a lógica do jogo.
        Atualiza a cobra e verifica a condição de pontuação/vitória."""

        if not self.death:
            self.update_direction()
            self.update_snake()
            self.check_death()
            self.check_apple()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.reset()

    def update_direction(self):
        """Observe as teclas e mude de direção."""

        if pyxel.btn(pyxel.KEY_UP):
            if self.direction is not DOWN:
                self.direction = UP
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.direction is not UP:
                self.direction = DOWN
        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.direction is not RIGHT:
                self.direction = LEFT
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.direction is not LEFT:
                self.direction = RIGHT

    def update_snake(self):
        """Mova a cobra com base na direção."""

        old_head = self.snake[0]
        new_head = Point(old_head.x + self.direction.x, old_head.y + self.direction.y)
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()

    def check_apple(self):
        """Check whether the snake is on an apple."""

        if self.snake[0] == self.apple:
            self.score += 1
            self.snake.append(self.popped_point)
            self.generate_apple()

            pyxel.play(0, 0)

    def generate_apple(self):
        """Gerar uma maçã aleatoriamente."""
        snake_pixels = set(self.snake)

        self.apple = self.snake[0]
        while self.apple in snake_pixels:
            x = randint(0, WIDTH - 1)
            y = randint(HEIGHT_SCORE + 1, HEIGHT - 1)
            self.apple = Point(x, y)

    def check_death(self):
        """Verifique se a cobra morreu (fora dos limites ou dobrou)."""

        head = self.snake[0]
        if head.x < 0 or head.y < HEIGHT_SCORE or head.x >= WIDTH or head.y >= HEIGHT:
            self.death_event()
        elif len(self.snake) != len(set(self.snake)):
            self.death_event()

    def death_event(self):
        """Mate o jogo (exiba a tela final)."""
        self.death = True  # Check having run into self

        pyxel.stop()
        pyxel.play(0, 1)

    ##############
    # Lógica do Desenho #
    ##############

    def draw(self):
        """Desenhe o plano de fundo, cobra, pontuação e maçã OU a tela final."""

        if not self.death:
            pyxel.cls(col=COL_BACKGROUND)
            self.draw_snake()
            self.draw_score()
            pyxel.pset(self.apple.x, self.apple.y, col=COL_APPLE)

        else:
            self.draw_death()

    def draw_snake(self):
        """Desenhe a cobra com uma cabeça distinta repetindo o deque."""

        for i, point in enumerate(self.snake):
            if i == 0:
                colour = COL_HEAD
            else:
                colour = COL_BODY
            pyxel.pset(point.x, point.y, col=colour)

    def draw_score(self):
        """Desenhe a pontuação no topo."""

        score = f"{self.score:04}"
        pyxel.rect(0, 0, WIDTH, HEIGHT_SCORE, COL_SCORE_BACKGROUND)
        pyxel.text(1, 1, score, COL_SCORE)

    def draw_death(self):
        """Desenhe uma tela em branco com algum texto."""

        pyxel.cls(col=COL_DEATH)
        display_text = TEXT_DEATH[:]
        display_text.insert(1, f"{self.score:04}")
        for i, text in enumerate(display_text):
            y_offset = (pyxel.FONT_HEIGHT + 2) * i
            text_x = self.center_text(text, WIDTH)
            pyxel.text(text_x, HEIGHT_DEATH + y_offset, text, COL_TEXT_DEATH)

    @staticmethod
    def center_text(text, page_width, char_width=pyxel.FONT_WIDTH):
        """Helper function for calculating the start x value for centered text."""

        text_width = len(text) * char_width
        return (page_width - text_width) // 2


###########################
# Música e Efeitos Sonoros #
###########################


def define_sound_and_music():
    """Defini MUSICAS E SOM."""

    # Sound effects
    pyxel.sound(0).set(
        notes="c3e3g3c4c4", tones="s", volumes="2", effects=("n" * 4 + "f"), speed=7
    )
    pyxel.sound(1).set(
        notes="f3 b2 f2 b1  f1 f1 f1 f1",
        tones="p",
        volumes=("2" * 2 + "4321"),
        effects=("n" * 7 + "f"),
        speed=9,
    )

    melody1 = (
        "c3 c3 c3 d3 e3 r e3 r"
        + ("r" * 8)
        + "e3 e3 e3 f3 d3 r c3 r"
        + ("r" * 8)
        + "c3 c3 c3 d3 e3 r e3 r"
        + ("r" * 8)
        + "b2 b2 b2 f3 d3 r c3 r"
        + ("r" * 8)
    )

    melody2 = (
        "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 c3c3c3c3 d3d3d3d3 e3e3e3e3"
        + "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 g2g2g2g2 c3c3c3c3 g2g2a2a2"
        + "rrrr e3e3e3e3 d3d3c3c3 b2b2c3c3"
        + "a2a2a2a2 c3c3c3c3 d3d3d3d3 e3e3e3e3"
        + "f3f3f3a3 a3a3a3a3 g3g3g3b3 b3b3b3b3"
        + "b3b3b3b4 rrrr e3d3c3g3 a2g2e2d2"
    )

    # Music
    pyxel.sound(2).set(
        notes=melody1 * 2 + melody2 * 2,
        tones="s",
        volumes=("2"),
        effects=("nnnsffff"),
        speed=20,
    )

    harmony1 = (
        "a1 a1 a1 b1  f1 f1 c2 c2"
        "c2 c2 c2 c2  g1 g1 b1 b1" * 3
        + "f1 f1 f1 f1 f1 f1 f1 f1 g1 g1 g1 g1 g1 g1 g1 g1"
    )
    harmony2 = (
        ("f1" * 8 + "g1" * 8 + "a1" * 8 + ("c2" * 7 + "d2")) * 3 + "f1" * 16 + "g1" * 16
    )

    pyxel.sound(3).set(
        notes=harmony1 * 2 + harmony2 * 2, tones="t", volumes="2", effects="f", speed=20
    )
    pyxel.sound(4).set(
        notes=("f0 r a4 r  f0 f0 a4 r" "f0 r a4 r   f0 f0 a4 f0"),
        tones="n",
        volumes="6622 6622 6622 6426",
        effects="f",
        speed=20,
    )

    pyxel.music(0).set([], [2], [3], [4])



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

def jogo1():
    Snake()
    game.show()

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
principal = uic.loadUi("pg1.ui")
cadastro = uic.loadUi("PGcad.ui")
login = uic.loadUi("PGLog.ui")
game = uic.loadUi("jogos.ui")
principal.BTcad.clicked.connect(pg_cad)
principal.BTlog.clicked.connect(log)
cadastro.BTCad1.clicked.connect(cadastro_jogador)
login.BTlog1.clicked.connect(logar)
game.jogo1.clicked.connect(Snake)


principal.show()
app.exec()


