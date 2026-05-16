#caracteres ilegais
#\
#txt = "We are the so-called "Vikings" from the north." #erro
txt = "We are the so-called \"Vikings\" from the north." #forma correta
print(txt)
isa = 'isa\'s home.'
print(isa) 
barra = "vai adicionar uma \\ (barra inversa)."
print(barra) 
ola = "Hello\nWorld!" #pula uma linha
print(ola) 
rer = "Hello\rWorld!" #mostra apenas o da frente
print(rer) 
tab = "Hello\tWorld!" #espaco
print(tab) 

erase = "Hello \bWorld!" #apaga o espaco
print(erase) 

oct = "\110\145\154\154\157" #retorna um valor octal
print(oct) 


hex = "\x48\x65\x6c\x6c\x6f" #retorna um valor hexadecimal
print(hex) 





