# Previsão de saída
lista = [10, 20, 30, 40]
lista.append(50)
lista.remove(20)
print(lista)
print(lista[2])


# Lista e operações
numeros = [2, 4, 6, 8, 10]
print(numeros [1 : 4])  # Printa 4, 6 e 8, pq ele vai do elemento 1, mas não conta o 4° (que seria o 10)
print(numeros[-1])  # Printa o ultimo elemento da lista, que é 10, se fosse -2, printaria 8
print (len(numeros))  # Diz o tamanho da lista, ou seja, 5 elementos


# Lista x Tupla
frutas = ["maça", "banana", "uva"]
tupla = tuple(frutas)  # O comando tuple, transforma uma lista em uma tupla
print(tupla)


# Dicionário
alunos = {
    "Ana": 8.5,
    "Pedro": 6.0,
    "Marcos": 9.0
          }
print(alunos["Marcos"])
alunos["Julia"] = 7.5  # Adicionar pessoa na lista, caso caía na prova
alunos["Pedro"] = 6.5  # Altera o valor na lista
print(alunos)

cidades = {
    "SC":["Joinville", "Jaraguá", "Blumenau"],
    "RS": ["Gravataí", "Inter", "Erechim"],
    "PR": ["Curitiba", "Toledo", "Maringá"]
}
print(cidades["PR"][2])  # Printa a cidade conforme o indice


# Adicionar nome nas listas e passar pra tupla
nomes = []
i = 0
while i < 4:
    nome = input("Diga 4 nomes: ")
    i += 1
    nomes.append(nome)
print(nomes)
tupla = tuple(nomes)
print(tupla)

# Exemplo do loop com o for

# for i in range (4):    
    # nome = input("sla: ")
    # nomes.append (nome)