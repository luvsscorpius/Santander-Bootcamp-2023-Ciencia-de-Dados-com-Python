ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Informe a quantidade de ativos: "))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input("Informe os ativos: ")
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.

ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.

for ativo in ativos:
    print(ativo)