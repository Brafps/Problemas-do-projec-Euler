'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
numero = 600851475143

# nessa parte do código, encontrei os divisores da variável número
lista_de_divisores = []             
for i in range(1,(numero + 1)//2):
    resto = numero%i
    if  resto == 0:
        quociente = numero//i
        lista_de_divisores.append(quociente)
        lista_de_divisores.append(i)
        if quociente <= i:
            break

# nessa parte do código, encontrei os divisores que são primos e peguei o maior.
lista_de_primos = []
n_de_divisores_de_i = 0
for i in lista_de_divisores:
    for x in lista_de_divisores:
        if (i % x) == 0:
            n_de_divisores_de_i = n_de_divisores_de_i + 1
    if n_de_divisores_de_i == 2:
        lista_de_primos.append(i)
        n_de_divisores_de_i = 0
    else:
        n_de_divisores_de_i = 0
print(max(lista_de_primos))