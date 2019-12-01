class objects:
    def __init__(self, nome, data, cluster):
        self.nome = nome
        self.data = data
        self.closest = self
        self.cluster = cluster


class ot:
    def __init__(self, a, b, y):
        self.a = a
        self.b = b
        self.y = y
