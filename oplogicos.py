"""
and --> retorna true se os dois valores forem verdade
or --> retorna true se um dos valores forem verdade
not --> se for true, vai retornar false, se for false, vai retornar true
"""


x = 5
print(x > 0 and x < 10)
#x>o true x<10 true = true

y = 11
print(y > 0 and y < 10)
#y>0true y<10 false = false

X = 5
print(X < 5 or X > 10)
#x eh menor q cinco ou x é maior que 10 = falso

Y = 5
print(Y < 6 or Y > 20)
#y eh meenor q cinco ou y eh maior q 20 = falso

z = 5

print(not(z > 3 and z < 10))
"verdade e verdade = verdade, mas barrado fica falso"
