# Os parâmetros que estão antes da barra são posicionais e os que estão depois são por nome
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Pálio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Inválido