
import mysql.connector
from treinador import Treinador, Pokedex
from pokedex import  Conexao
from batalha import batalha
conexao = Conexao()
treinador = Treinador()
pokedex = Pokedex()
captura = batalha()
conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mateus4321",
            database="projeto_integrador")
cursor = conexao.cursor()

while True:
    
    try:
        
        print("          Menu de login da Pokedex          \n\n\
            Qual apção desejada\n\
        \n1: Registra jogador\n\
        \n2: Fazer login")

        escolha = int(input("\n\nDigite a opção desejada: "))

        if escolha == 1:
            treinador.registrar_treinador()
            
            while True:
            
                try:
            
                    id_treinador = int(input('Digite seu ID para comtinua: '))
                    sql = f"SELECT * FROM treinadores where id_treinador = '{id_treinador}';"
                    cursor.execute(sql)
                    treinador = cursor.fetchone()
                
                    if id_treinador == treinador[0]:
                        pokedex.escolher_primero_pokemon(id_treinador)
                        break
                
                    elif id_treinador != treinador[0]:
                        print("ID Não encontrado")
                
                except:
                    print("Errou tente novamente")
                
                
        elif escolha == 2:
            pokedex.login()
            break
            
        else:
            print("Opção invalida")
            
    except:
        print("Escolha invalida.")

while True:

    try:
        
        print("          Menu da pokedex          \n\n\
            Qual apção desejada\n\
        \n1: Captura pokémon\n\
        \n2: Renomea pokémon\n\
        \n3: Lista pokémon capturados\n\
        \n4: Procura pokémon\n\
        \n5: Sollta pokémon\n\
        \n6: Sair do Menu\n")
        
        escolha = int(input("Digite a opção desejada: "))
        
        if escolha == 1:
            captura.captura_pokemon()
            
        elif escolha == 2:
            pokedex.nomea_pokemon()
            
        elif escolha == 3:
            pokedex.lista_pokemon_capturados()
        
        elif escolha == 4:
            pokedex.exibir_pokemon()
            
        elif escolha == 5:
            pokedex.solta_pokemon()
            
        elif escolha == 6:
            break
        
        else:
            print("\nEscolha invalida")
        
    except:
        print("\nVoçê errou tente novamente")
        
conexao.close()