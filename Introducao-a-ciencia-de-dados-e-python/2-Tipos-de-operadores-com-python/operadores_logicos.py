# Na condição AND para ser true tudo tem que ser true
# Na condição OR apenas um tem que ser true

print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(False and False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#true
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#true
print(exp_2)