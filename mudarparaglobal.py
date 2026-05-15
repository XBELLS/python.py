
x = "awesome"

def myfunc():
  global x #altera o valor da variavel
  x = "fantastic"

myfunc()

print("Python is " + x)
