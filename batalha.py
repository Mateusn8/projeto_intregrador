from pokedex import Conexao
import random
from treinador import Pokedex
treinador = Pokedex
class batalha(Pokedex):
    
    def captura_pokemon(self):
        numero = random.randint(1, 100)
        
        
        while True:
            
            try:
            
                if numero <= 10: 
                    sql = "SELECT * FROM pokemon_lendarios;"
                    self.cursor.execute(sql)
                    lista = self.cursor.fetchall()
                    pokemon = random.choice(lista)
                    print(f"Um {pokemon[1]}, se ferrou\nID: {pokemon[0]}")
                    return False
            
                else: 
                    sql = "SELECT * FROM pokemon;"
                    self.cursor.execute(sql)
                    lista = self.cursor.fetchall()
                    pokemon_selvagen = random.choice(lista)
                    self.vidaInimigo = pokemon_selvagen[4]
                    print(f"Um {pokemon_selvagen[1]}\nAtaque: {pokemon_selvagen[2]}\nDefesa: {pokemon_selvagen[3]}\nVida: {pokemon_selvagen[4]}, deseja batalhar?")
                    numero = random.randint(1, 100)
                    escolha = input('\n\nDigite s pra sim ou n pra não: ')
                    enfraquecido = self.vidaInimigo*(20/100)

                    if escolha == 's':
                        sql = f"SELECT * FROM pokemon_coletados where id_treinador = {self.id_treinador}"
                        self.cursor.execute(sql)
                        lista = self.cursor.fetchall()
                        
                        for pokemon in lista:
                            print(f"ID: {pokemon[1]}\nPokemon: {pokemon[2]}")
                        escolha = int(input('Insira o ID do pokémon de escolha: '))

                        for pokemon in lista:        
                            
                            if escolha == pokemon[0]:
                                sql = f"SELECT FROM pokemon WHERE numero_na_pokedex = {escolha}"
                                self.cursor.execute(sql)
                                pokemon = self.cursor.fetchone()
                                self.vida = pokemon[4]
                                print(f"Pokemon: {pokemon[1]}\nAtaque: {pokemon[2]}\nDefesa: {pokemon[3]}\nVida: {pokemon[4]}\n\n")
                                
                                while True:

                                    print("Deseja atacar, defender ou fugir")
                                    opcao = input("\nDigite a opção desejada: ")
                    
                                    if opcao == "atacar":
                                        self.ataque = random.randint(pokemon[2]-5,pokemon[2]+5)
                                        
                                        print(f"Voçe deu {ataque} de dano")
                                        self.vidaInimigo -= self.ataque

                                        if self.vidaInimigo <= enfraquecido:
                                            print("O pokemon esta enfraquecido, deseja captura?")
                                            captura = input("s para capturar: ")

                                            if captura == "s":
                                                self.importa_pokemon(self.id_treinador, pokemon[0], pokemon[1])
                                                print("parabens voçê capturou o pokemon")
                                                return True
                                            
                                            else:
                                                return True

                                    if opcao == "defender":
                                        ataque = random.randint(pokemon_selvagen[2]-5,pokemon_selvagen[2]+5)
                                        print(f"Você tomou o dano de {ataque}")
                                       
                                        if self.vida > ataque:
                                            print("A defesa foi efetiva")
                                        
                                        if self.vida <= enfraquecido:
                                            print("Seu pokemon esta enfraquecido deseja troca")

                                        else:
                                            print("A defesa não foi efetiva")

                                    if opcao == 'fugir':
                                        print ("Covarde")
                                        return False

                    if escolha == 'n':
                        print("O pokemon fugiu")
                        return False

                    if numero <= 20:
                        print("O pokemon fugiu, mas sorte da proxima vez")
                        
                    else:
                        treinador = int(input("Qual é seu ID: "))
                        self.importa_pokemon(treinador, pokemon[0], pokemon[1])
                        print("parabens voçê capturou o pokemon")
                        return True
            
            except:
                print('Voçê errou, tente novamente')