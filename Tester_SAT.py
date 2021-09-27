import pygame
from pygame.locals import *
from sys import exit
from Classes import *

pygame.init()

largura = 640
altura = 480

pca = Poligono([300, 200], 4, ((200, 400), (400, 400), (400, 200), (200, 200)))
print(pca)

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
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    if pygame.key.get_pressed()[K_RIGHT]:
        pca.atualiza_pos_x(1)
    if pygame.key.get_pressed()[K_LEFT]:
        pca.atualiza_pos_x(-1)
    if pygame.key.get_pressed()[K_DOWN]:
        pca.atualiza_pos_y(1)
    if pygame.key.get_pressed()[K_UP]:
        pca.atualiza_pos_y(-1)

    pygame.draw.polygon(tela, (255, 0, 0), pca.vertices)
    # pygame.draw.rect(tela, (255, 0, 0), (pca.x, pca.y, 40, 40))
    pygame.display.update()
