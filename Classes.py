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
        self.vel_x = 0
        self.vel_y = 0

    def get_num_vert(self):
        return self.num_vert

    def get_vertices(self):
        return self.vertices

    def get_one_vertice(self, index):
        return self.vertices[index]

    def get_vel_x(self):
        return self.vel_x

    def get_vel_y(self):
        return self.vel_y

    def atualiza_vel(self, v_x, v_y):
        self.vel_x = v_x
        self.vel_y = v_y

    def parar(self):
        self.vel_x = 0
        self.vel_y = 0

    def __str__(self):
        return 'Objeto.origem: (' + str(self.get_x()) + ' ,' + str(self.get_y()) + ')\n' \
               'Objeto.n_Vert= ' + str(self.num_vert) + \
               '\nVertices: ' + str(self.vertices)


# ----------------- Teste da classe ------------------
# obj = Poligonos([1, 2], 3, ((4, 5), (5, 7), (8, 9)))
# print(obj)
