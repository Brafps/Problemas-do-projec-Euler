'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

quantidade_i = 10000

num_primo_l = [2]
num_testado_i = 2
posicao_i = 0

while posicao_i < quantidade_i:
  contador_i = 0
  for num_primo in num_primo_l:
    if num_testado_i % num_primo == 0:
      num_testado_i += 1
    else:
      contador_i += 1
      if contador_i > posicao_i:
        posicao_i += 1
        num_primo_l.append(num_testado_i)
print(num_primo_l[-1])