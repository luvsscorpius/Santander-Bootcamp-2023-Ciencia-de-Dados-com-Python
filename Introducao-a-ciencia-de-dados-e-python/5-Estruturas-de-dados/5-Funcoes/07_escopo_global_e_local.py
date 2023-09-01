salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    print(salario)


salario_bonus(500)  # 2500