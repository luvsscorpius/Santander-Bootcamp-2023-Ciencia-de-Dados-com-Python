nome = "and"

print(nome.upper()) # Maiúsculo
print(nome.lower()) # Minúsculo
print(nome.title()) # Título

texto = " Hello World   "

print(texto.strip()) # Remove todos os espaços
print(texto.lstrip()) # Remove os espaços da esquerda
print(texto.rstrip()) # Remove os espaços da direita

menu = "Python"

print("###" + menu + "###" )
print(menu.center(10))
print("-".join(menu))