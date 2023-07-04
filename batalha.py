from pokedex import Conexao
import random

class batalha(Conexao):
    
    def __init__(self):
        super().__init__()
    
    def captura_pokemon(self):
        sql = "SELECT * FROM pokemon UNION ALL SELECT * FROM pokemon_lendarios;"
        self.cursor.execute(sql)
        lista = self.cursor.fetchall()
        pokemon = random.choice(lista)
        numero = random.randint(1, 100)
        
        while True:
            
            if numero <= 10: 
                pokemon = random.choice(lista) 
                print(f"Um {pokemon[1]}, se ferrou\nID: {pokemon[0]}")
                return False
        
            else: 
                pokemon = random.choice(lista[:151]) 
                print(f"Um {pokemon[1]}, degeja captura ?\nID: {pokemon[0]}")
                escolha = input('\n\nDidite s pra sim ou n pra não')
                
                if escolha == 'n':
                    print("O pokemon fugiu")
                    
                else:
                    print("parabens voçê capturou o pokemon")
                