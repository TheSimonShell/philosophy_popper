# Problema 2

# Obter uma password aleatória

import string
import random

# Guarda o conjunto de caracteres disponiveis

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Obtem o número de caracteres necessários para a password e guarda na variavel user_input

user_input = input("Quantos caracteres quer na sua password? ")

# Cria um ciclo

while True:
    try:
        characters_number = int(user_input) # Define characters_number como um número a partir da variavel user_input

        if characters_number < 8: # Se characters_number for inferior a 8, executa
            print("Deve ser, no mínimo, 8 caracteres.")
            user_input = input("Insira novamente, quantos caracteres quer na sua password? ")

        else: # Se não for inferior a 8, executa
            break # Quebra o ciclo
    except: # Se for dado algo que não um número, executa
        print("Por favor, insira somente o número de caracteres que quer na sua password.")
        user_input = input("Insira novamente, quantos caracteres quer na sua password? ")

random.shuffle(s1) # Baralha a lista s1
random.shuffle(s2) # Baralha a lista s2
random.shuffle(s3) # Baralha a lista s3
random.shuffle(s4) # Baralha a lista s4

part1 = round(characters_number * (30/100)) # Obtém a primeira parte da password com o produto da multiplicação: characters_number x 30%
part2 = round(characters_number * (20/100)) # Obtém a segunda parte da password com o produto da multiplicação: characters_number x 20%

result = [] # Cria uma array(lista) vazia para o resultado da password

for x in range(part1): # Em cada caracter no alcance do número dado na part1, executa, sendo x o número atual
    result.append(s1[x % len(s1)]) # Adiciona o caracter x na lista s1 a lista result (cíclico)
    result.append(s2[x % len(s2)]) # Adiciona o caracter x na lista s2 a lista result (cíclico)

for x in range(part2): # Em cada caracter no alcance do número dado na part2, executa, sendo x o número atual
    result.append(s3[x % len(s3)]) # Adiciona o caracter x na lista s3 a lista result (cíclico)
    result.append(s4[x % len(s4)]) # Adiciona o caracter x na lista s4 a lista result (cíclico)

random.shuffle(result) # Baralha a lista result

password = "".join(result) # Une a lista em uma string (frase)
print("A sua nova password é: ", password) # Imprime o resultado final
