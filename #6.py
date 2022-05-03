'''
he sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
soma = 0
soma_dos_quadrados = 0
for i in range(1, 101):
    soma_dos_quadrados = soma_dos_quadrados + i**2
    soma = soma + i
print(soma**2 - soma_dos_quadrados)