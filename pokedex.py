import mysql.connector

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus1234",
            database="projeto_integrado"
        )
        self.cursor = self.conexao.cursor()

class professor:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = idade

    def pokedex(self):
        ...
    
    
    
