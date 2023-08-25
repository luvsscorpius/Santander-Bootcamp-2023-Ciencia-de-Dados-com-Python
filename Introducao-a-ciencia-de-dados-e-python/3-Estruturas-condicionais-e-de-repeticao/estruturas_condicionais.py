maior_idade = 18
idade_especial = 17

# Primeiro exemplo
idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")

if idade < maior_idade:
    print("Menor de idade, não pode tirar a CNH")

# Segundo exemplo
idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Menor de idade, não pode tirar a CNH")

# Terceiro exemplo

idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
elif idade == idade_especial:
    print("Pode fazer a aula teórica, mas não pode fazer as aulas práticas")
else:
    print("Menor de idade, não pode tirar a CNH")