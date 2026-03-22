# Problema 2

# Obter uma password aleatória

import string
import random

# Guarda o conjunto de caracteres disponiveis

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("Quantos caracteres quer na sua password? ")

while True:
    try:
        characters_number = int(user_input)

        if characters_number < 8:
            print("Deve ser, no mínimo, 8 caracteres.")
            user_input = input("Insira novamente, quantos caracteres quer na sua password? ")

        else:
            break
    except:
        print("Por favor, insira somente o número de caracteres que quer na sua password.")
        user_input = input("Insira novamente, quantos caracteres quer na sua password? ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)

password = "".join(result)
print("A sua nova password é: ", password)
