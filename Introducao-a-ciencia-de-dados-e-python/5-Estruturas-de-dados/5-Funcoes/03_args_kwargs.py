# *args
def somar(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(somar(1, 2, 3))

# **kwargs
def mostrar_infos(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_infos(Nome='And', Idade=25, Cidade='São Paulo')

# Combinação
def funcao_completa(arg1, *args, **kwargs):
    print(f'Arg1: {arg1}')
    print("args:", args)
    print("kwargs:", kwargs)

funcao_completa(10,20, 30, Nome="And", Profissão="Programador", idade=19)

