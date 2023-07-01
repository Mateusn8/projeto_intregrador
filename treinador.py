import mysql.connector
import time
from pokedex import conexao

class Treinador(conexao):
    def __init__(self, nome, idade, cidade):
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        

    def registrar_treinador(self):
        sql = "INSERT INTO treinadores (nome, idade, cidade) VALUES (%s, %s, %s)"
        val = (self.nome, self.idade, self.cidade)
        print('treinador registrado')
        self.cursor.execute(sql, val)
        self.conexao.commit()
    
    def pegar_id(self):
        self.cursor.execute(f"select * from treinadores where nome = '{self.nome}'")
        treinador = self.cursor.fetchone()
        return treinador[0]
    
      
class Pokedex(conexao):
        
    def escolher_primero_pokemon(self,idTreiner):
        pokedex = Pokedex()
        pokemon1 = pokedex.procura_pokemon(1)
        pokemon2 = pokedex.procura_pokemon(4)
        pokemon3 = pokedex.procura_pokemon(7)


        print(f"Escolha um dos seguintes pokémons para ser o seu primeiro:")
        print(f"1 - {pokemon1[1]} (Tipo: {pokemon1[2]}, ataque: {pokemon1[3]})")
        print(f"2 - {pokemon2[1]} (Tipo: {pokemon2[2]}, ataque: {pokemon2[3]})")
        print(f"3 - {pokemon3[1]} (Tipo: {pokemon3[2]}, ataque: {pokemon3[3]})")
        
        escolha = None
        tempo_inicial = time.localtime()
        while True:
            escolha = input('digite o número do pokémon que você quer escolhe: ')
            
            if escolha in ['1', '2', '3']:
                escolha = int(escolha)
                match escolha:
                    case 2: escolha = 4
                    case 3: escolha = 7
                break
            
            else:
                print(' entrada invalida. digite 1, 2 ou 3.')
                tempo_atual = time.localtime()
                if float(time.strftime("%S",tempo_atual)) - float(time.strftime("%S",tempo_inicial)) > 30:
                    print("Tempo esgotado. Um pikachu será escolhido pelo sistema.")
                    escolha = 25
                    break
        
        self.cursor.execute(f"select * from pokemon where numero_na_pokedex = {escolha}")
        pokemon = self.cursor.fetchone()
        self.importa_pokemon(idTreiner, escolha, pokemon[1])
        print(f"Parabéns! Você escolheu o {pokemon[1]} como seu primeiro pokémon.")
                             
   
    
    def solta_pokemon(self, id_pokemon):
        sql = "DELETE FROM pokemon_coletados WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon solto com sucesso.")
    
    def nomea_pokemon(self):
        id_pokemon = Pokedex.lista_pokemon_capturados()
        print(id_pokemon)
        escolha = input(int('Insira o número do pokémon de escolha: '))
        escolha = id_pokemon[escolha]
        print(escolha)
        escolha = escolha[1]
        print(escolha)
        novo_nome = input(str('Insira o novo nome do pokémon: '))
        sql = "UPDATE pokemon_coletados SET nome = %s WHERE id_pokemon = %s"
        valores = (novo_nome, escolha)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        

    def lista_pokemon_capturados(self, id_treinador):
        lista = []
        sql = f"SELECT * FROM pokemon_coletados WHERE id_treinador = {id_treinador}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado: 
            lista.append(linha)
        print(lista)
    
    def procura_pokemon(self, id):
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            return resultado
        
    def exibir_pokemon(self, id):
        sql =f"SELECT * FROM pokemon_coletados WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
             print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nhabilidades: {resultado[6]}")

    def importa_pokemon(self, id_treinador, id_pokemon, nome_pokemon):
        self.cursor.execute(f"insert into pokemon_coletados (id_treinador,id_pokemon,nome_pokemon) values ({id_treinador},{id_pokemon},'{nome_pokemon}')")
        self.conexao.commit()
    
    


