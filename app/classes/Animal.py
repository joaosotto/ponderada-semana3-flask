class Animal:
    def __init__(self, nome, especie, felicidade=50, livre=True):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade
        self.livre = livre

    def __repr__(self):
        return f"{self.nome} ({self.especie}, Felicidade: {self.felicidade})"