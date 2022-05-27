'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

''''
Note que para a solução desse problemas, devemos lembrar que, se fizermos a soma simples, estaremos contando o múltiplos de 15 duas vezes. Logo, temos que pensar em uma maneira de resolver esse problema.
'''

soma = 0                       
for i in range(1000):
    if (i%3 == 0 or i%5 == 0): 
        soma = soma+i          
print(soma)