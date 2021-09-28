from typing import *
from math import sqrt, acos, pi
import numpy as np


class Ponto2D:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_par(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def subtrai_vetor_do_ponto(self, a):
        if not isinstance(a, Vetor2D):
            raise TypeError
        return Ponto2D([self.x + a.x, self.y + a.y])

    def soma_vetor_ao_ponto(self, a):
        if not isinstance(a, Vetor2D):
            raise TypeError
        return Ponto2D([self.x + a.x, self.y + a.y])

    def __str__(self):
        return str(self.get_par())


class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_par(self):
        return self.x, self.y

    def diferenca_entre_pontos(self, a: Ponto2D, b: Ponto2D):
        if not (isinstance(a, Ponto2D) and isinstance(b, Ponto2D)):
            raise TypeError
        self.x = a.x - b.x
        self.y = a.y - b.y

    def ret_diferenca_entre_pontos(self, a: Ponto2D):
        return Vetor2D(self.x - a.x, self.y - a.y)

    def soma_vetores(self, a, b):
        if not (isinstance(a, Vetor2D) and isinstance(b, Vetor2D)):
            raise TypeError
        self.x = a.x + b.x
        self.y = a.y + b.y

    def subtrai_vetores(self, a, b):
        if not (isinstance(a, Vetor2D) and isinstance(b, Vetor2D)):
            raise TypeError
        self.x = a.x - b.x
        self.y = a.y - b.y

    def produto_por_escalar(self, escalar):
        self.x *= escalar
        self.y *= escalar

    def produto_escalar(self, v):
        return np.array(self.get_par()) @ np.array(v.get_par())

    def modulo_vetor(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normaliza_vetor(self):
        c = self.modulo_vetor()
        self.x /= c
        self.y /= c

    def vetor_direcao(self):
        self.normaliza_vetor()
        if self.y > 0:
            return acos(self.x)
        else:
            return acos(self.x) + pi

    def rotaciona_vetor_90(self):
        a = self.x
        self.x = self.y
        self.y = -a

    def __str__(self):
        return str(self.get_par())


class Matriz2x2:
    def __init__(self, m: List):
        self.elementos = [m[:2], m[2:]]

    def __str__(self):
        return f'Matriz: {self.elementos[0]}\n        {self.elementos[1]}'


# noinspection PyChainedComparisons
class Poligono:
    def __init__(self, cor, org_dist, num_vert, vertices):
        self.org_dist = Vetor2D(org_dist[0], org_dist[1])
        self.num_vert = num_vert
        self.vertices = []
        self.cor = cor
        for i in range(len(vertices)):
            self.vertices.append(Ponto2D(vertices[i]))

    def get_cor(self):
        return self.cor

    def get_num_vert(self):
        return self.num_vert

    def get_vertices(self):
        lista = []
        for i in range(self.num_vert):
            pontos = [self.vertices[i].x, self.vertices[i].y]
            lista.append(pontos)
        return lista

    def get_one_vertice(self, index):
        return self.vertices[index]

    def set_cor(self, cor):
        self.cor = cor

    def atualiza_pos_x(self, x):
        self.org_dist.x += x

    def atualiza_pos_y(self, y):
        self.org_dist.y += y

    def get_vertices_plot(self):
        vertices_plot = []
        for i in range(self.num_vert):
            vertices_plot.append(self.vertices[i].soma_vetor_ao_ponto(self.org_dist).get_par())
        return vertices_plot

    def get_one_vertice_plot(self, index):
        return self.vertices[index].soma_vetor_ao_ponto(self.org_dist)

    # Teste de intersecção de Axis Aligned Bounding Boxes. (AABB)
    def check_colisao(self, obj):
        if not isinstance(obj, Poligono):
            raise TypeError
        # Achando os pontos máximos e mínimos de X e Y para o primeiro Polígono
        a_min = Ponto2D([self.get_one_vertice_plot(0).x, self.get_one_vertice_plot(0).y])
        a_max = Ponto2D([self.get_one_vertice_plot(0).x, self.get_one_vertice_plot(0).y])
        for i in range(1, self.get_num_vert()):
            if self.get_one_vertice_plot(i).x < a_min.x:
                a_min.set_x(self.get_one_vertice_plot(i).x)
            if self.get_one_vertice_plot(i).y < a_min.y:
                a_min.set_y(self.get_one_vertice_plot(i).y)

            if self.get_one_vertice_plot(i).x > a_max.x:
                a_max.set_x(self.get_one_vertice_plot(i).x)
            if self.get_one_vertice_plot(i).y > a_max.y:
                a_max.set_y(self.get_one_vertice_plot(i).y)

        # Achando os pontos máximos e mínimos e X e Y para o segundo Polígono
        b_min = Ponto2D([obj.get_one_vertice_plot(0).x, obj.get_one_vertice_plot(0).y])
        b_max = Ponto2D([obj.get_one_vertice_plot(0).x, obj.get_one_vertice_plot(0).y])
        for i in range(1, obj.get_num_vert()):
            if obj.get_one_vertice_plot(i).x < b_min.x:
                b_min.set_x(self.get_one_vertice_plot(i).x)
            if obj.get_one_vertice_plot(i).y < b_min.y:
                b_min.set_y(self.get_one_vertice_plot(i).y)

            if obj.get_one_vertice_plot(i).x > b_max.x:
                b_max.set_x(self.get_one_vertice_plot(i).x)
            if obj.get_one_vertice_plot(i).y > b_max.y:
                b_max.set_y(self.get_one_vertice_plot(i).y)

        # Se falso, os polígonos não se colidem.
        # Caso verdadeiro, tem a possibilidade de estarem colidindo.
        if a_min.x <= b_max.x and b_min.x <= a_max.x and \
           a_min.y <= b_max.y and b_min.y <= a_max.y:

            # print('AABB não consegue concluir\nEntrando no SAT')
            # print(a_min, a_max, b_min, b_max)

            # Testa usando as arestas do polígino A como referência
            for i in range(self.get_num_vert()):
                aresta = Vetor2D(0, 0)

                if not i+1 >= self.get_num_vert():
                    aresta.diferenca_entre_pontos(self.get_one_vertice_plot(i+1), self.get_one_vertice_plot(i))
                else:
                    aresta.diferenca_entre_pontos(self.get_one_vertice_plot(0), self.get_one_vertice_plot(i))

                aresta.rotaciona_vetor_90()
                # print(aresta)
                amax = None
                amin = None
                bmax = None
                bmin = None

                # Encontra os valores de min e max para o polígono A usando a nova aresta
                for j in range(self.get_num_vert()):
                    dot = aresta.produto_escalar(self.get_one_vertice_plot(j))
                    if amax is None or dot > amax:
                        amax = dot
                    if amin is None or dot < amin:
                        amin = dot

                # Encontra os valores de min e max para o polígono B usando a nova aresta
                for j in range(obj.get_num_vert()):
                    dot = aresta.produto_escalar(obj.get_one_vertice_plot(j))
                    if bmax is None or dot > bmax:
                        bmax = dot
                    if bmin is None or dot < bmin:
                        bmin = dot

                # print(amin, amax, bmin, bmax)

                # Identifica se há um gap entre os polígonos por este ângulo
                if (amin > bmax or amin < bmin) and (bmin > amax or bmin < amin):
                    return False

            # Testa usando as arestas do polígino B como referência
            for i in range(obj.get_num_vert()):
                aresta = Vetor2D(0, 0)

                if not i+1 >= obj.get_num_vert():
                    aresta.diferenca_entre_pontos(obj.get_one_vertice_plot(i+1), obj.get_one_vertice_plot(i))
                else:
                    aresta.diferenca_entre_pontos(obj.get_one_vertice_plot(0), obj.get_one_vertice_plot(i))

                aresta.rotaciona_vetor_90()
                # print(aresta)

                amax = None
                amin = None
                bmax = None
                bmin = None

                # Encontra os valores de min e max para o polígono A usando a nova aresta
                for j in range(self.get_num_vert()):
                    dot = aresta.produto_escalar(self.get_one_vertice_plot(j))
                    if amax is None or dot > amax:
                        amax = dot
                    if amin is None or dot < amin:
                        amin = dot

                # Encontra os valores de min e max para o polígono B usando a nova aresta
                for j in range(obj.get_num_vert()):
                    dot = aresta.produto_escalar(obj.get_one_vertice_plot(j))
                    if bmax is None or dot > bmax:
                        bmax = dot
                    if bmin is None or dot < bmin:
                        bmin = dot

                # print(amin, amax, bmin, bmax)

                # Identifica se há um gap entre os polígonos por este ângulo
                if (amin > bmax or amin < bmin) and (bmin > amax or bmin < amin):
                    return False

            return True

        else:
            # print('Não está colidindo')
            # print(a_min, a_max, b_min, b_max)
            return False

    def __str__(self):
        return 'org_dist: ' + str(self.org_dist.get_par()) + \
               '\nNumero de vertices: ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.get_vertices())


# ----------------- Teste das classes ------------------
# teste onde não colidem
'''verticesA = ((13, 10), (13, 3), (6, 3), (6, 10))
verticesB = ((14, 18), (15, 11), (10, 13))
poligonoA = Poligono([0, 0], len(verticesA), verticesA)
poligonoB = Poligono([0, 0], len(verticesB), verticesB)
if PoligonoA.check_colisao(PoligonoB):
    print('Colide!!!')
else:
    print('Não colide!!!')'''

# teste onde colidem
'''verticesA = ((11, 10), (11, 3), (4, 3), (4, 10))
verticesB = ((13, 13), (8, 9), (7, 15))
poligonoA = Poligono([0, 0], len(verticesA), verticesA)
poligonoB = Poligono([0, 0], len(verticesB), verticesB)
if PoligonoA.check_colisao(PoligonoB):
    print('Colide!!!')
else:
    print('Não colide!!!')'''

'''
v1 = Vetor2D(0, 2)
v2 = Vetor2D(2, 0)
d = v1.produto_escalar(v2)'''
