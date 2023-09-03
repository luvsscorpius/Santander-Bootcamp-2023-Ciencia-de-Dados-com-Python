# Entrada de dados
saldo_total = int(input("Informe o seu saldo total: "))
valor_saque = int(input("Informe o valor do seu saque: "))

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if valor_saque <= saldo_total:
    saldo_total = saldo_total - valor_saque
    print(f"Saque realizado com sucesso. Novo saldo: {saldo_total}")
else:
    print("Saldo insuficiente. Saque não realizado!")