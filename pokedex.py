import mysql.connector

class Pokemon:
    def __init__(self, name):
        self.name = name
db = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="sua_base_de_dados")

class professor:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = idade

    def pokedex(self):
        ...
    
    
    
