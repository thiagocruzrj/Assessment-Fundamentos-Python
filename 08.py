from random import randint
import pygame

pygame.init()

largura_tela = 800
altura_tela = 600

# cores
amarelo = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

tela = pygame.display.set_mode((largura_tela, altura_tela))

tela.fill(white)

quadrados_iniciais = 1

button = pygame.draw.circle(tela, amarelo, [int(largura_tela / 2), 40], 40)

fonte = pygame.font.Font(None, 24)
texto = fonte.render("Clique", 1, black)
tela.blit(texto, [380, 38])

lista = []

class Quadradinho():
  def __init__(self):
    self.largura = 50
    self.altura = 50
    self.x = randint(0, largura_tela - self.largura)
    self.y = randint(20, altura_tela - self.altura)
    self.position = (self.x, self.y)
    self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
    self.cor = (amarelo)

  def desenha(self, tela, cor):
    pygame.draw.rect(tela, cor or self.cor, self.area)

def randomSquare():
  q = Quadradinho()
  q.desenha(tela, amarelo)

  for i in lista:
    if len(lista) > 1:
      if q.area == i.area:
        print(i.position, q.position)
        print(i.position)
        lista.remove(i)
        a = Quadradinho()
        pygame.draw.rect(tela, white, i.area)
        print('removido')
  lista.append(q)

terminou = False
while not terminou:

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      terminou = True
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
      pos = pygame.mouse.get_pos()
      if button.collidepoint(pos):
        randomSquare()

pygame.display.quit()
pygame.quit()