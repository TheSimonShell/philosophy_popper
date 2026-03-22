# Problema 3

# Obter o número e lista de anagramas numa palavra

from math import factorial
from collections import Counter

def count_anagrams(word): # Cria uma função count_anagrams com a entrada da variável word, para a palavra a verificar
    n = len(word) # Obtém o tamanho da palavra
    counts = Counter(word) # Conta quantas vezes cada letra aparece na palavra

    denominator = 1 # Variável para o denominador da fórmula dos anagramas
    for count in counts.values(): # Percorre o número de ocorrências de cada letra
        denominator *= factorial(count) # Multiplica pelo fatorial de cada ocorrência

    return factorial(n) // denominator # Retorna o total de anagramas possíveis


def generate_anagrams(word): # Cria uma função generate_anagrams com a entrada da variável word, para gerar anagramas
    counts = Counter(word) # Conta quantas vezes cada letra aparece
    result = [] # Lista onde serão guardados os anagramas

    def backtrack(path): # Função auxiliar recursiva para construir os anagramas
        if len(path) == len(word): # Se o tamanho do caminho for igual ao tamanho da palavra
            result.append("".join(path)) # Junta as letras e adiciona à lista de resultados
            return
        
        for char in counts: # Percorre cada letra disponível
            if counts[char] > 0: # Se ainda houver ocorrências dessa letra
                counts[char] -= 1 # Usa uma ocorrência dessa letra
                path.append(char) # Adiciona a letra ao caminho atual
                
                backtrack(path) # Chama recursivamente para continuar a construir
                
                path.pop() # Remove a última letra (backtrack)
                counts[char] += 1 # Restaura a ocorrência da letra

    backtrack([]) # Inicia o processo com um caminho vazio
    return sorted(result) # Retorna a lista ordenada de anagramas


word = input("Escreve uma palavra: ").upper() # Obtém a palavra para os anagramas

total = count_anagrams(word) # Executa a função count_anagrams e guarda o número de anagramas

verification = input("Quer que dê a lista de anagramas possíveis? (s/N)") # Pergunta se quer ver a lista

if verification == "s": # Se o utilizador quiser ver os anagramas
    anagrams = generate_anagrams(word) # Gera a lista de anagramas
    print(f"\nTotal de anagramas: {total}") # Mostra o número total
    print("\nLista de anagramas:")
    for a in anagrams:
        print(a) # Mostra cada anagrama
else:
    print(f"\nTotal de anagramas: {total}") # Mostra apenas o número total
