from math import pi


class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_par(self):
        return [self.x, self.y]


class Funcs(Ponto2D):
    def diferenca_entre_pontos(self, a, b):
        self.x = a.x - b.x
        self.y = a.y - b.y

    def soma_vetor_ao_ponto(self, a, b):
        self.x = a.x + b.x
        self.y = a.y + b.y

    def subtrai_vetor_do_ponto(self, a, b):
        self.x = a.x - b.x
        self.y = a.y - b.y

    def soma_vetores(self, a, b):
        self.x = a.x + b.x
        self.y = a.y + b.y

    def subtrai_vetores(self):
        pass


class Matriz2x2:
    def __init__(self, m):
        self.elementos = m


class Poligonos(Ponto2D, Funcs):
    def __init__(self, origem, num_vert, vertices):
        Ponto2D.__init__(self, origem[0], origem[1])
        self.num_vert = num_vert
        self.vertices = vertices

    def get_num_vert(self):
        return self.num_vert

    def get_vertices(self):
        return self.vertices

    def get_one_vertice(self, index):
        return self.vertices[index]

    def atualiza_pos_x(self, x):
        self.x += x

    def atualiza_pos_y(self, y):
        self.y += y

    def plot(self, tela: tuple):
        pass

    def __str__(self):
        return 'Origem: ' + str(self.get_par()) + \
               'Numero de vertices= ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.vertices)


# ----------------- Teste da classe ------------------
# obj = Poligonos([1, 2], 3, ((4, 5), (5, 7), (8, 9)))
# print(obj)
