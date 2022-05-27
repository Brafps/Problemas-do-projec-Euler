'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

for i_num in range (999*999, 10000, -1):
    s_num = str(i_num)
    s_inv_num = s_num[::-1]
    if s_num == s_inv_num:
        for div in range(999 - 1, 100, -1):
            if (i_num % div == 0) and (len(str(i_num//div)) == 3):
                print(i_num)
                break


# Idéia que não valeu seguir.
'''    
Um amigo me deu uma ajuda e melhoramos a solução para que parasse na resposta pedida.

def funcao1(): 
    for i_num in range (999*999, 10000, -1): 
        s_num = str(i_num) 
        s_inv_num = s_num[::-1] 
        if (funcao2(i_num, s_num, s_inv_num)): 
            print(i_num) 
            return 
         
 
def funcao2(i_num, s_num, s_inv_num): 
    if (s_num == s_inv_num): 
        for div in range(999 - 1, 100, -1): 
            if (i_num % div == 0) and (len(str(i_num//div)) == 3): 
                return True 
        return False 
 
 
funcao1()
'''