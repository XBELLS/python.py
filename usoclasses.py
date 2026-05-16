class myclass(): #cria uma class nomeada myclass() -->molde q cria objetos
  def __len__(self): #len é usado pra ver o tamanho de um objeto
    return 0 #vai retornar valor 0  false
    return 1 #vai retornar valor 1 - true
#porem ele apenas le sempre o primeiro return, ent nesse caso eh false
myobj = myclass() #criação de um objeto em myclass()
print(bool(myobj)) #printa o valor booleano do objeto

