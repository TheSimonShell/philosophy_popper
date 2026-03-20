# Problema 1

# Obter números primos até 10,000

# Criar função is_prime com a entrada de argumento variável n
def is_prime(n):
    if n > 1: # Se n for maior que 1
        for i in range(2, n): # Por cada número i de 2 à variável n, em que i é o número atual do ciclo, executa
            if n % i == 0: # Se n der resto 0 ao dividir com i, não é primo
                return False
        else: # Se não cumprir as condições acima, é primo
            return True


def primes_up_to(limit): # Criar função primes_up_to com a entrada de argumento variável limit
    primes = [] # Cria array (lista) vazia para guardar os números primos
    for num in range(2, limit + 1): # Por cada 
        if is_prime(num):
            primes.append(num)
    return primes


# Executar
print(primes_up_to(10000))