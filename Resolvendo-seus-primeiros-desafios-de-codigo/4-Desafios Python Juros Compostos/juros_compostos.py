valor_inicial = float(input("Informe o valor inicial do seu investimento: "))
taxa_juros = float(input("Informe a taxa de juros: "))
periodo = int(input("Informe o periodo: "))

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

def calcular_juros(valor_inicial, taxa_juros, periodo):
    taxa_juros_decimal = taxa_juros
    valor_final = valor_inicial * (1 + taxa_juros_decimal) ** periodo
    return valor_final

valor_final = calcular_juros(valor_inicial, taxa_juros, periodo)


print("Valor final do investimento: R$", round(valor_final, 2))