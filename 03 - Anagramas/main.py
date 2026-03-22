# Problema 3

# Obter o número e lista de anagramas numa palavra

from math import factorial
from collections import Counter
import itertools

def count_anagrams(word):
    n = len(word)
    counts = Counter(word)

    denominator = 1
    for count in counts.values():
        denominator *= factorial(count)

    return factorial(n) // denominator

def generate_anagrams(word):
    return sorted(set("".join(p) for p in itertools.permutations(word)))

word = input("Escreve uma palavra: ").upper()

total = count_anagrams(word)
anagrams = generate_anagrams(word)

print(f"\nTotal de anagrams: {total}")
verification_of_printanagrams = input("Quer que dê a lista de anagramas possíveis? (s/N)")
if verification_of_printanagrams == "s":
    print("\nLista de anagramas:")
    for a in anagrams:
        print(a)
else:
    pass
