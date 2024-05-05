import unittest
from Animal import Animal
from Recinto import Recinto
from Zoologico import Zoologico

class TesteZoologico(unittest.TestCase):
    def setUp(self):
        # Preparação comum para todos os testes nesta classe
        self.zoo = Zoologico()
        self.recinto_pug = self.zoo.criar_recinto('pug')
        self.animal = Animal('cachorro', 'pug', 50, True)
        self.recinto_pug.animais.append(self.animal)

    def teste_alimentar_animais(self):
        # Testando o aumento de felicidade dos animais da espécie 'pug'
        self.zoo.alimentar_animais('pug', 10)
        self.assertEqual(self.animal.felicidade, 60)

    def teste_adicionar_animal(self):
        # Testando a adição de um novo animal ao recinto correspondente
        novo_animal = Animal('gato', 'pug', 30, True)
        adicionado = self.zoo.adicionar_animal(novo_animal)
        self.assertIs(adicionado, novo_animal)
        self.assertFalse(novo_animal.livre)
        self.assertIn(novo_animal, self.recinto_pug.animais)

    def teste_receber_visitantes(self):
        # Testando a receita gerada com base na condição dos recintos e animais
        self.recinto_pug.bem_cuidado = True
        self.animal.felicidade = 60  # Assegurar que a felicidade seja alta o suficiente
        resultado = self.zoo.receber_visitantes(10)
        self.assertEqual(resultado, "Receita gerada: R$100")

if __name__ == '__main__':
    unittest.main()