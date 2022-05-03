'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def mmc(a, b, c):
    for i in range(min(a,b), a*b*c + 1):
        if i%a == 0 and i%b == 0 and i%c == 0:
            break
    return i
b = 2520
c = 11
for i in range(1, 6):
    b = mmc(b, c, c+1)
    c += 2
print(b)