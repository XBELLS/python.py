#:= associa o valor a variavel e usa na expressao com o strinf

numbers = [1, 2, 3, 4, 5] #1 ate 5 é atribuido a variavel numbers

if (count := len(numbers)) > 3: #len ve o tamanho e verifica se tem mais de 3 elementos
    print(f"a lista tem {count} elementos")
else: 
    print(f"A lista nao tem mais de 3, ela tem {count} elementos")
