x = "awesome" #variavel global

def myfunc():
    x = "fantastic" #variavel local
    print("Python is",  x)
    
myfunc()

print("Python is", x)
