# Problema 3

# Obter o número e lista de anagramas numa palavra

from math import factorial
from collections import Counter
import itertools

def count_anagrams(word): # Cria uma função count_anagrams com a entrada de variavel word, para a palavra a verificar
    n = len(word) # Obtem o tamanho da palavra
    counts = Counter(word) # Verifica o número de ocorrências de letras, ou seja, quantas vezes uma letra aparece na palavra, por exemplo, na palavra Somente, S: 1 vez, O: 1 vez, M: 1 vez, E: 2 vezes, N: 1 vez e T: 1 vez

    denominator = 1 # Fórmula para obter anagramas possíveis
    for count in counts.values():
        denominator *= factorial(count)

    return factorial(n) // denominator

def generate_anagrams(word): # Cria uma função generate_anagrams com a entrada de variavel word, para a palavra a permutar
    return sorted(set("".join(p) for p in itertools.permutations(word))) # Apresenta permutaçoes (anagramas) da palavra

word = input("Escreve uma palavra: ").upper() # Obtem a palavra para os anagramas

total = count_anagrams(word) # Executa a função count_anagrams e guarda o número de anagramas na variavel total
anagrams = generate_anagrams(word) # Executa a função generate_anagrams e guarda a lista de anagramas na variavel anagrams

print(f"\nTotal de anagrams: {total}") # Apresenta o número total de anagramas
verification_of_printanagrams = input("Quer que dê a lista de anagramas possíveis? (s/N)") # Pergunta se quer que seja apresentado a lista de anagramas
if verification_of_printanagrams == "s": # Se sim
    print("\nLista de anagramas:")
    for a in anagrams:
        print(a) # Apresenta a lista de anagramas
else:
    pass # Se não, para o programa
