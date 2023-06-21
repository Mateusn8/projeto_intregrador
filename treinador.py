import mysql.connector

class treinador:
    def __init__(self, nome, idade, cidade, pokedex_treinador):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.pokedex = pokedex_treinador
       
class Pokedex:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus1234",
            database="projeto_integrado"ss
        )
        self.cursor = self.conexao.cursor()
        
    def adicionar_pokemon(self, pokemon):
        self.pokedex_treinador.append(pokemon)
        
    def lista_pokemon(self):
        self.pokedex_treinador = []

    def nomea_pokemon(self):
        ...

    def procura_pokemon(self, nome):
        for pokemon in self.pokemon_list:
            if pokemon.nome.lower() == nome.lower():
                return pokemon
        return None
    
    def atualiza_pokemon(self):
        ...
    
    def fecha_conexao(self):
        self.cursor.close()
        self.conexao.close()


