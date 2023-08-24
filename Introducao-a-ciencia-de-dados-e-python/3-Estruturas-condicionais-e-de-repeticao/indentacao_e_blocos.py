def sacar(valor):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print(F"R$ {valor} sacado com sucesso")
        print(F"Valor atual da conta: R$ {saldo}")

sacar(100)