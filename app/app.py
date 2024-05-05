from flask import Flask
from Animal import Animal
from Zoologico import Zoologico
from Recinto import Recinto

app= Flask(__name__)

@app.route("/criar-animais")
def criar_animal(nome, especie, felicidade):
    animal = Animal(nome, especie, felicidade)
    return animal

@app.route("/criar-recinto")
def criar_recinto(especie, bem_cuidado):
    recinto = Recinto(especie, bem_cuidado)
    return recinto

@app.route("/adicionar-animal")
def adicionar_animal(animal):
    zoo = Zoologico()
    return zoo.adicionar_animal(animal)

        
@app.route("/alimentar-animais")
def alimentar_animais(especie, quantidade):
    zoo = Zoologico()
    return zoo.alimentar_animais(especie, quantidade)

@app.route("/receber-visitas")
def receber_visitas(visitantes):
    zoo = Zoologico()
    return zoo.receber_visitantes(visitantes)

if __name__ == "__main__":
    app.run(debug=True)