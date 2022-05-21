'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


# A ideia aqui foi começar pelo valor c e ir descendo até o valor a fazendo os condicionais.

for c in range(0,1001):
  for b in range(0,1001):
    if b < c:
      for a in range(0,1001):
        if a < b and b < c:
          if a + b + c == 1000:
            x = a**2
            y = b**2
            z = c**2
            if x + y == z:
              print(a, b, c)
              print(a*b*c)