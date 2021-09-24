import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = 300
y = 200
step = 1

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste Separating Axis Theorem')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                pass

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 40))
    pygame.display.update()
