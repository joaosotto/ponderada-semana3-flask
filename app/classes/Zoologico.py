from Recinto import Recinto

class Zoologico:
    def __init__(self):
        self.recintos = []

    def criar_recinto(self, especie):
        recinto = Recinto(especie)
        self.recintos.append(recinto)
        return recinto

    def alimentar_animais(self, especie, quantidade):
        for recinto in self.recintos:
            if recinto.especie == especie:
                for animal in recinto.animais:
                    animal.felicidade += quantidade

    def adicionar_animal(self, animal):
        for recinto in self.recintos:
            if animal.especie == recinto.especie and animal.livre == True:
              recinto.animais.append(animal)
              animal.livre = False
              return animal

    def receber_visitantes(self, numero_de_visitantes):
        receita = 0
        for recinto in self.recintos:
            if recinto.bem_cuidado and all(animal.felicidade > 50 for animal in recinto.animais):
                receita += numero_de_visitantes * 10
        return f"Receita gerada: R${receita}"