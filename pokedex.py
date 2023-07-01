import mysql.connector

class conexao:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus4321",
            database="projeto_integrador"
        )
        self.cursor = self.conexao.cursor()

    def fecha_conexao(self):
        self.cursor.close()
        self.conexao.close()

class professor(conexao):
    def __init__(self, nome, idade, cidade):
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
       
    def lista_geracao_pokemon(self):
        geracao = input(int('Insira a geração a ser exibida: '))
        sql = f'SELECT * FROM pokemon where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        for pokemon in pokemons:
            print(pokemon)

    def informacoes_pokemon(self):
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nhabilidades: {resultado[6]}")
            
    def informacoes_pokemon_lemdario(self):
        sql =f"SELECT * FROM pokemon_lendarios WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nhabilidades: {resultado[6]}")
            
    def lista_geracao_pokemon_lendarios(self):
        geracao = input(int('Insira a geração a ser exibida: '))
        sql = f'SELECT * FROM pokemon_lendarios where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        for pokemon_lendarios in pokemons:
            print(pokemon_lendarios)

    def deleta_pokemon(self, id_pokemon):
        sql = "DELETE FROM pokemon WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon deletado com sucesso.")

    def deleta_pokemon_lendario(self, id_pokemon):
        sql = "DELETE FROM pokemon WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon lendario deletado com sucesso.")

    def atualiza_pokemon(self, id_pokemon, novo_nome):
        sql = f"UPDATE {self.nome} SET nome = %s WHERE id_pokemon = %s"
        valores = (novo_nome, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit()    

class Pokemon(conexao):
    
    def __init__(self, nome, ataque, defesa, vida, geracao, habilidades):
        super().__init__()
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.geracao = geracao    
        self.habilidades = habilidades

class lendaria(Pokemon):
    def __init__(self, nome, ataque, defesa, vida, geracao, habilidades):
        super().__init__(nome, ataque, defesa, vida, geracao, habilidades)
