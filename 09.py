from random import randint
import pygame

pygame.init()

largura_tela = 800
altura_tela = 600

FPS = 200

amarelo = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

radius = 40

quadrados_iniciais = 1

fonte = pygame.font.Font(None, 24)

def desenhaButton(button_position):
    return pygame.draw.circle(tela, amarelo, [button_position[0], button_position[1]], radius)

def desenhaTexto(text_position):
    texto = fonte.render("Clique", 1, black)
    return tela.blit(texto, (text_position[0], text_position[1]))


lista = []

class Quadradinho():
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = randint(0, largura_tela-self.largura)
        self.y = randint(20, altura_tela-self.altura)
        self.position = (self.x, self.y)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (amarelo)

    def desenha(self, tela, cor):
        pygame.draw.rect(tela, cor or self.cor, self.area)

def randomSquare():
    q = Quadradinho()
    q.desenha(tela, amarelo)

    for i in lista:
        print(i.area, q.area)
        if len(lista) > 1:
            if q.area.collidepoint(i.position):
                print(i.position, q.position)
                print(i.position)
                lista.remove(i)
                a = Quadradinho()
                pygame.draw.rect(tela, white, i.area)
                pygame.draw.rect(tela, white, q.area)
                print('removido')
    lista.append(q)


def verificaColisão(q):
    for i in lista:
        if len(lista) > 1:
            if q.colliderect(i.area):
                lista.remove(i)
                a = Quadradinho()
                pygame.draw.rect(tela, white, i.area)
                print('removido')


def moveCircle(teclas, button_position, button):
    if teclas[0] and button_position[1] > 0:
        button_position[1] -= 2
    elif teclas[2] and button_position[1] < 600:
        button_position[1] += 2
    if teclas[1] and button_position[0] > 0:
        button_position[0] -= 2
    elif teclas[3]and button_position[0] < 800:
        button_position[0] += 2

    verificaColisão(button)
    return button_position


def moveText(teclas, text_position):
    if teclas[0] and text_position[1] > 0:
        text_position[1] -= 2
    elif teclas[2] and text_position[1] < 600:
        text_position[1] += 2
    if teclas[1] and text_position[0] > 0:
        text_position[0] -= 2
    elif teclas[3]and text_position[0] < 800:
        text_position[0] += 2
    return text_position

def main():

    global tela

    teclas = [False, False, False, False]

    button_position = [int(largura_tela/2), 40]
    text_position = [380, 38]

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    tela.fill(white)
    terminou = False

    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    randomSquare()

            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    teclas[0] = True
                elif event.key == 97:
                    teclas[1] = True
                elif event.key == 115:
                    teclas[2] = True
                elif event.key == 100:
                    teclas[3] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    teclas[0] = False
                elif event.key == pygame.K_a:
                    teclas[1] = False
                elif event.key == pygame.K_s:
                    teclas[2] = False
                elif event.key == pygame.K_d:
                    teclas[3] = False

        button = desenhaButton(button_position)
        button_position = moveCircle(teclas, button_position, button)

        text_position = moveText(teclas, text_position)
        text = desenhaTexto(text_position)

        moveCircle(teclas, button_position, button)
        moveText(teclas, text_position)

        pygame.display.update()

    pygame.display.quit()

    pygame.quit()


if __name__ == '__main__':
    main()
