from treinador import Treinador, Pokedex

nome = input('nome: ')
idade = int(input('idade: '))
cidade = input('cidade: ')

treinador1 = Treinador(nome, idade, cidade)
treinador1.registrar_treinador()


pokedex = Pokedex()

pokedex.escolher_primero_pokemon(treinador1.pegar_id())
pokedex.fecha_conexao()

