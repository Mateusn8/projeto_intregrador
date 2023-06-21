import mysql.connector


class pokemon_selvagen:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus1234",
            database="projeto_integrado"
        )
        self.cursor = self.conexao.cursor()
        
        