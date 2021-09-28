import pygame
from pygame.locals import *
from sys import exit
from Classes import *

pygame.init()

largura = 960
altura = 680
vel = 4

verticesA = ((100, 100), (-100, 100), (-100, -100), (100, -100))
verticesB = ((100, -100), (-100, -100), (0, 100))
poligonoA = Poligono((255, 0, 0), [400, 500], len(verticesA), verticesA)
poligonoB = Poligono((0, 0, 255), [400, 500], len(verticesB), verticesB)
print(poligonoA.get_vertices_plot())

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
            if event.key == K_SPACE:
                if poligonoA.check_colisao(poligonoB):
                    poligonoA.set_cor(0, 255, 0)
                else:
                    poligonoA.set_cor(255, 0, 0)

    if pygame.key.get_pressed()[K_RIGHT]:
        poligonoB.atualiza_pos_x(vel)
    if pygame.key.get_pressed()[K_LEFT]:
        poligonoB.atualiza_pos_x(-vel)
    if pygame.key.get_pressed()[K_DOWN]:
        poligonoB.atualiza_pos_y(vel)
    if pygame.key.get_pressed()[K_UP]:
        poligonoB.atualiza_pos_y(-vel)

    if pygame.key.get_pressed()[K_d]:
        poligonoA.atualiza_pos_x(vel)
    if pygame.key.get_pressed()[K_a]:
        poligonoA.atualiza_pos_x(-vel)
    if pygame.key.get_pressed()[K_s]:
        poligonoA.atualiza_pos_y(vel)
    if pygame.key.get_pressed()[K_w]:
        poligonoA.atualiza_pos_y(-vel)

    pygame.draw.polygon(tela, poligonoA.get_cor(), poligonoA.get_vertices_plot())
    pygame.draw.polygon(tela, poligonoB.get_cor(), poligonoB.get_vertices_plot())
    pygame.display.update()
