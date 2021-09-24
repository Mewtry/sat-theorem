from math import pi


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

    def __str__(self):
        return str(self.get_par())


class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_par(self):
        return self.x, self.y


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


class Poligonos:
    def __init__(self, org_dist, num_vert, vertices):
        self.org_dist = Vetor2D(org_dist[0], org_dist[1])
        self.num_vert = num_vert
        self.vertices = []
        for i in range(len(vertices)):
            self.vertices.append(Ponto2D(vertices[i]))

    def get_num_vert(self):
        return self.num_vert

    def get_vertices(self):
        return self.vertices

    def get_one_vertice(self, index):
        return self.vertices[index]

    def atualiza_pos_x(self, x):
        self.org_dist.x += x

    def atualiza_pos_y(self, y):
        self.org_dist.y += y

    def plot(self, tela: tuple):
        pass

    def __str__(self):
        return 'org_dist: ' + str(self.org_dist.get_par()) + \
               '\nNumero de vertices= ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.vertices)


# ----------------- Teste da classe ------------------
'''tupladetuplas = [(4, 5), (5, 7), (8, 9)]
obj = Poligonos([1, 2], 3, tupladetuplas)
print(obj.vertices)
print(obj)
print(tupladetuplas)'''
