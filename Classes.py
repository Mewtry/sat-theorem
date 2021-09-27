from typing import *
from math import sqrt, acos, pi


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

    def subtrai_vetor_do_ponto(self, a, b):
        if not (isinstance(a, Ponto2D) and isinstance(b, Vetor2D)):
            raise TypeError
        self.x = a.x - b.x
        self.y = a.y - b.y

    def soma_vetor_ao_ponto(self, a, b):
        if not (isinstance(a, Ponto2D) and isinstance(b, Vetor2D)):
            raise TypeError
        self.x = a.x + b.x
        self.y = a.y + b.y

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

    def produto_escalar_ret_orig(self, escalar):
        self.x *= escalar
        self.y *= escalar

    def dot_product(self, a):
        return self.x * a.x + self.y * a.y

    def comprimento_vetor(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normaliza_vetor(self):
        c = self.comprimento_vetor()
        self.x /= c
        self.y /= c

    def vetor_direcao(self):
        self.normaliza_vetor()
        if self.y > 0:
            return acos(self.x)
        return acos(self.x) + pi

    def __str__(self):
        return str(self.get_par())


class Matriz2x2:
    def __init__(self, m: List):
        self.elementos = [m[:2], m[2:]]

    def __str__(self):
        return f'Matriz: {self.elementos[0]}\n        {self.elementos[1]}'


class Poligono:
    def __init__(self, org_dist, num_vert, vertices):
        self.org_dist = Vetor2D(org_dist[0], org_dist[1])
        self.num_vert = num_vert
        self.vertices = []
        for i in range(len(vertices)):
            self.vertices.append(Ponto2D(vertices[i]))

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

    def atualiza_pos_x(self, x):
        self.org_dist.x += x

    def atualiza_pos_y(self, y):
        self.org_dist.y += y

    def plot(self, tela: tuple):
        pass

    def check_colisao(self, obj):
        # Primeiro teste de intersecção de Axis Aligned Bounding Boxes. (AABB)
        min_a = Ponto2D([self.get_one_vertice(0).x, self.get_one_vertice(0).y])
        max_a = Ponto2D([self.get_one_vertice(0).x, self.get_one_vertice(0).y])
        for i in range(1, self.get_num_vert()):
            if self.get_one_vertice(i).x < min_a.x:
                min_a.set_x(self.get_one_vertice(i).x)
            if self.get_one_vertice(i).y < min_a.y:
                min_a.set_y(self.get_one_vertice(i).y)

            if self.get_one_vertice(i).x > max_a.x:
                max_a.set_x(self.get_one_vertice(i).x)
            if self.get_one_vertice(i).y > max_a.y:
                max_a.set_y(self.get_one_vertice(i).y)

        min_b = Ponto2D([obj.get_one_vertice(0).x, obj.get_one_vertice(0).y])
        max_b = Ponto2D([obj.get_one_vertice(0).x, obj.get_one_vertice(0).y])
        for i in range(1, obj.get_num_vert()):
            if obj.get_one_vertice(i).x < min_b.x:
                min_b.set_x(self.get_one_vertice(i).x)
            if obj.get_one_vertice(i).y < min_b.y:
                min_b.set_y(self.get_one_vertice(i).y)

            if obj.get_one_vertice(i).x > max_b.x:
                max_b.set_x(self.get_one_vertice(i).x)
            if obj.get_one_vertice(i).y > max_b.y:
                max_b.set_y(self.get_one_vertice(i).y)

        if min_a.x < max_b.x and min_b.x < max_a.x and min_a.y < max_b.y and min_b.y < max_a.y:

            print('Há a possibilidade de estar colidindo')
            print(min_a, max_a, min_b, max_b)

        else:
            print('Não está colidindo')
            print(min_a, max_a, min_b, max_b)

    def __str__(self):
        return 'org_dist: ' + str(self.org_dist.get_par()) + \
               '\nNumero de vertices: ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.get_vertices())


# ----------------- Teste das classes ------------------
tupladetuplas = ((0, 0), (0, 2), (2, 2), (2, 0))
teste1 = Poligono([1, 1], len(tupladetuplas), tupladetuplas)
print(teste1)

vert = ((2, 0), (2, 2), (4, 2), (4, 0))
teste2 = Poligono([2, 1], len(vert), vert)
print(teste2)

teste1.check_colisao(teste2)



# m = Matriz2x2([1, 2, 3, 4])
# print(m)
'''
v= Vetor2D(0, 0)
a = Ponto2D([4, 4])
b = Ponto2D([1, 1])
print(v)'''