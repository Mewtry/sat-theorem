import pygame
from pygame.locals import *
from sys import exit
from Classes import *

pygame.init()

largura = 960
altura = 680
vel = 3
cor_pol_A = 255, 255, 0
cor_pol_B = 0, 0, 255
cor_colisao_A = 255, 0, 0
cor_colisao_B = 0, 255, 0

verticesA = ((100, 100), (-100, 100), (-100, -100), (100, -100))
verticesB = ((100, -100), (-100, -100), (0, 100))
poligonoA = Poligono(cor_pol_A, [400, 500], len(verticesA), verticesA)
poligonoB = Poligono(cor_pol_B, [400, 500], len(verticesB), verticesB)


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
                pass

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

    if poligonoA.check_colisao(poligonoB):
        poligonoA.set_cor(cor_colisao_A)
        # poligonoB.set_cor(cor_colisao_B)
    else:
        poligonoA.set_cor(cor_pol_A)
        # poligonoB.set_cor(cor_pol_B)

    pygame.draw.polygon(tela, poligonoA.get_cor(), poligonoA.get_vertices_plot())
    pygame.draw.polygon(tela, poligonoB.get_cor(), poligonoB.get_vertices_plot())
    pygame.display.update()
