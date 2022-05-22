'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# Aqui, tentei aproveitar o programa que fiz para o problema 7, mas ele ficou extremamente demorado, fui pesquisar algo na biblioteca math.

import math

def verificador_primo(num):
    teste = 2
    while teste <= math.sqrt(num):
        if (num % teste) < 1:
            return False
        teste += 1
    return True
soma = 0
for numero in range(2, 2000001):
  if verificador_primo(numero) == True:
    soma = soma + numero
print(soma)