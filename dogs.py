######################## 1 MONTANDO DATASET   ################################################  
#Caracteristicas
#e fofinho?
#Tem uma orelhinha pequena?
#Faz miau?

#Se SIM = 1 / Se NAO = 0

animalmisterioso1 = [1, 1, 1]
amimalmisterioso2 = [1, 0, 1]
animalmisterioso3 = [0, 1, 1]
animalmisteriosos4 = [1, 1, 0]
animalmisterioso5 = [0, 1, 0]
animalmisterioso6 = [0, 1, 0]

dados = [animal1, animal2, animal3, animal4, animal5, animal6]

#Se GATO = 1 / Se CACHORRO = -1
marcacoes = [1, 1, 1, -1, -1, -1]

######################## 2 CRIANDO MODELO   ################################################  
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

######################## 3 FAZENDO PREDICOES   ################################################ 
animal_misterioso1 = [1, 1, 1]
animal_misterioso2 = [1, 0, 0]
animal_misterioso3 = [0, 0, 1]

teste = [animal_misterioso1, animal_misterioso2, animal_misterioso3]

marcacoes_teste = [1, -1, 1]

######################## 4 OBSERVANDO RESULTADOS   ################################################ 
resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)


total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("1: Gato e -1: Cachorro")

print("Resultado: ")
print(resultado)

print ("Marcacoes: ")
print(marcacoes_teste)

print("Diferencas: ")
print(diferencas)


print("Taxa de acerto do Algoritmo: ")
print(taxa_de_acerto)
