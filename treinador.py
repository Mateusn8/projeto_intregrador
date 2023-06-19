import mysql.connector

class treinador:
    def __init__(self, nome, idade, cidade, pokedex_treinador):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.pokedex = pokedex_treinador

class Pokedex:
    def adicionar_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def __init__(self):
        self.pokemon_list = []

    def adicionar_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def nomea_pokemon(self):
        ...

    def procura_pokemon(self, nome):
        for pokemon in self.pokemon_list:
            if pokemon.nome.lower() == nome.lower():
                return pokemon
        return None
    
    def atualiza_pokemon(self):
        ...
    


db = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="sua_base_de_dados"
)
