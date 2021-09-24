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


class Poligonos(Ponto2D):
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

    def __str__(self):
        return 'Objeto.origem: (' + str(self.get_x()) + ' ,' + str(self.get_y()) + ')\n' \
               'Objeto.n_Vert= ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.vertices)


# ----------------- Teste da classe ------------------
# obj = Poligonos([1, 2], 3, ((4, 5), (5, 7), (8, 9)))
# print(obj)
