#valores booleanos
#true or False

print(10 > 9) #retorna um valor booleano
print(10 == 9)
print(10 < 9)

a = 17
b = 22

if(a>b):
    print("a é maior do que b")
else:
    print("b é maior do que a")
    
print(bool("Hello")) #quando usa o bool(), verifica se eh f ou v
print(bool(15))

x = "Hello"
y = 15

print(bool(x)) #a maioria eh verdadeira
print(bool(y))

#casos a parte que dao false

z = 0 
print(bool(z)) #quando um numero eh 0
print(bool(False)) #false = false
print(bool(None))#vazio eh falso
print(bool(0)) #0 eh falso
print(bool("")) #vazio com aspas dupla eh falso
print(bool(())) #vazio com parenteses eh falso
print(bool([])) #vazio com colchetes eh falso
print(bool({})) #vazio com chaves eh falso
