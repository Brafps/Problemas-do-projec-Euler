'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


# Lembrando que aqui é o máximo - 1
max = 1000000 


num = 2
max_num_termos_i = 1


# Aqui é onde o interpretador coloca cada número a ser testado
for x in range(3,max):
  termo_i = 1
  i = x
 

# Nessa parte temos as condições de collatz sendo empregada. 
  while x > 1:
    if x % 2 == 0:
      x /= 2
      termo_i += 1
    else:
      x = 3*x+1
      termo_i += 1
  
# Nesse condicional, guardamos o número de maior quantidade de termos  
  if termo_i > max_num_termos_i:
    max_num_termos_i = termo_i
    num = i

# Relatório final
print(f'O número que gera a maior sequencia de Collatz é o número {num} com {max_num_termos_i} termos.')