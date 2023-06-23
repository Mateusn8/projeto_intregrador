import mysql.connector
import random 

class treinador:
    def __init__(self, nome, idade, cidade, pokedex_treinador):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.pokedex = pokedex_treinador
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus1234",
            database="projeto_integrado"
        )
        self.cursor = self.conexao.cursor()
    
    def pokedex_treinador(self):
        sql = "CREATE TABLE pokemon_coletados (id_treinador INT PRIMARY KEY, nome_treinador VARCHAR(50), id_pokemon INT, nome_pokemon VARCHAR(50))"
        self.cursor.execute(sql)
        self.conexao.commit()       
class Pokedex:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus1234",
            database="projeto_integrado"
        )
        self.cursor = self.conexao.cursor()
        
    def adicionar_pokemon(self, pokemon):
        self.pokemon = pokemon
        sql = "INSERT INTO pokemon_coletados (id_pokemon,id_treinador)VALUES(%s,%s)"
        valores = (self.id_pokemon,self.id_treinador)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        print("Pokémon capturado com sucesso.")
        
    def lista_pokemon(self):
        sql = "SELECT * FROM pokemon_coletados"
        self.cursor.execute(sql)
        pokemons_capturados = self.cursor.fetchall()
        for pokemon in pokemons_capturados:
            print(pokemon)
    
    def solta_pokemon(self, id_pokemon):
        sql = "DELETE FROM pokemon_coletados WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon solto com sucesso.")
    
    def nomea_pokemon(self, id_pokemon, novo_nome):
        sql = f"UPDATE {self.nome} SET nome = %s WHERE id_pokemon = %s"
        valores = (novo_nome, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        
    def procura_pokemon(self, nome):
        sql = "SELECT * FROM pokemon_coletados WHERE nome = %s"
        valor = (nome)
        self.cursor.execute(sql, valor)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
        
        else:
            print(resultado)
            
    
    def fecha_conexao(self):
        self.cursor.close()
        self.conexao.close()


