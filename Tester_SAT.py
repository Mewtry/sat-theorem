import pygame
from pygame.locals import *
from sys import exit
from Classes import *

pygame.init()

largura = 640
altura = 480

pca = Poligonos([300, 200], 4, ((-1, 1), (1, 1), (1, -1), (-1, -1)))
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

    '''if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                pca.atualiza_vel_x(1)
            if event.key == K_LEFT:
                pca.atualiza_vel_x(-1)
            if event.key == K_UP:
                pca.atualiza_vel_y(-1)
            if event.key == K_DOWN:
                pca.atualiza_vel_y(1)
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                pca.atualiza_vel_x(0)
                print('Soltou Direita ou Esquerda')
            if event.key == K_UP or event.key == K_DOWN:
                pca.atualiza_vel_y(0)
                print('Soltou cima ou baixo')
    pca.atualiza_pos()'''

    pygame.draw.rect(tela, (255, 0, 0), (pca.x, pca.y, 40, 40))
    pygame.display.update()
