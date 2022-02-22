"""
Teclas de controle ← ↑ → ↓

Q: Sai do jogo
R: Recomeça o jogo

"""

from collections import deque, namedtuple
from random import randint
import pyxel

# Classe de conveniência para coordenadas
Point = namedtuple("Point", ["x", "y"])


#############
# Constants #
#############

COL_BACKGROUND = 10
COL_BODY = 3
COL_HEAD = 11
COL_DEATH = 11
COL_APPLE = 8

TEXT_DEATH = ["Fim de Jogo", "(Q)UIT", "(R)ESTART"]
COL_TEXT_DEATH = 0
HEIGHT_DEATH = 1

WIDTH = 45
HEIGHT = 50

HEIGHT_SCORE = pyxel.FONT_HEIGHT
COL_SCORE = 0
COL_SCORE_BACKGROUND = 11

UP = Point(0, -1)
DOWN = Point(0, 1)
RIGHT = Point(1, 0)
LEFT = Point(-1, 0)

START = Point(5, 5 + HEIGHT_SCORE)



# Jogo #


class Snake:
    """A classe que configura e executa o jogo."""

    def __init__(self):
        """Inicia o pyxel, configura as variáveis iniciais do jogo e o executa."""

        pyxel.init(WIDTH, HEIGHT, title="Snake!", fps=20, capture_scale=4)
        self.Atualiza()
        pyxel.run(self.update, self.design)

    def Atualiza(self):
        """Inicia as variáveis-chave (direction, snake, apple, score, etc.)"""

        self.direction = RIGHT
        self.snake = deque()
        self.snake.append(START)
        self.death = False
        self.score = 0
        self.gera_maca()

        pyxel.playm(0, loop=True)

    # Lojica do jogo #

    def update(self):
        """ Atualizar a lógica do jogo.
            Atualiza a cobra e verifica a condição de pontuação/vitória. """

        if not self.death:
            self.atualiza_direcao()
            self.atualiza_cobra()
            self.verifica_morte()
            self.verifica_maca()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.Atualiza()

    def atualiza_direcao(self):
        """Identifica as teclas e muda de direção."""

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

    def atualiza_cobra(self):
        """Move a cobra com base na direção identificadas."""

        old_head = self.snake[0]
        new_head = Point(old_head.x + self.direction.x, old_head.y + self.direction.y)
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()

    def verifica_maca(self):
        """Verifique se a cobra pegou uma maçã."""

        if self.snake[0] == self.apple:
            self.score += 1
            self.snake.append(self.popped_point)
            self.gera_maca()

            pyxel.play(0, 0)

    def gera_maca(self):
        """Gere uma maçã aleatoriamente."""
        snake_pixels = set(self.snake)

        self.apple = self.snake[0]
        while self.apple in snake_pixels:
            x = randint(0, WIDTH - 1)
            y = randint(HEIGHT_SCORE + 1, HEIGHT - 1)
            self.apple = Point(x, y)

    def verifica_morte(self):
        """Verifique se a cobra morreu (fora dos limites ou dobrou)."""

        head = self.snake[0]
        if head.x < 0 or head.y < HEIGHT_SCORE or head.x >= WIDTH or head.y >= HEIGHT:
            self.morte()
        elif len(self.snake) != len(set(self.snake)):
            self.morte()

    def morte(self):
        """Interrompe o jogo (exiba a tela final)."""
        self.death = True  # Verifique ter executado em si mesmo

        pyxel.stop()
        pyxel.play(0, 1)
  
    # Logica de desenho #
  

    def design(self):
        """Desenha o background, snake, score e apple OU a end screen."""

        if not self.death:
            pyxel.cls(col=COL_BACKGROUND)
            self.design_cobra()
            self.design_pontuacao()
            pyxel.pset(self.apple.x, self.apple.y, col=COL_APPLE)

        else:
            self.design_morte()

    def design_cobra(self):
        """Desenhe a cobra com uma cabeça distinta repetindo o deque."""

        for i, point in enumerate(self.snake):
            if i == 0:
                colour = COL_HEAD
            else:
                colour = COL_BODY
            pyxel.pset(point.x, point.y, col=colour)

    def design_pontuacao(self):
        """Desenhe a pontuação no topo."""

        score = f"{self.score:04}"
        pyxel.rect(0, 0, WIDTH, HEIGHT_SCORE, COL_SCORE_BACKGROUND)
        pyxel.text(1, 1, score, COL_SCORE)

    def design_morte(self):
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
        """Função auxiliar para calcular o valor inicial x para texto centralizado."""

        text_width = len(text) * char_width
        return (page_width - text_width) // 2

