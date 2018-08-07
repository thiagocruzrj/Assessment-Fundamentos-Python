from random import randint
import pygame, random

pygame.init()

largura_tela = 800
altura_tela = 600

black = (0, 0, 0)
tela = pygame.display.set_mode((largura_tela, altura_tela))

tela.fill(black)

terminou = False
while not terminou:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pygame.draw.rect(tela, (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255)), (randint(0, 800), randint(0, 600), 50, 50))
        if event.type == pygame.KEYDOWN and event.key == 32:
            pygame.draw.rect(tela, (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255)), (randint(0, 800), randint(0, 600), 50, 50))
    print(event)

pygame.display.quit()
pygame.quit()