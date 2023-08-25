conta_normal = False
conta_universitaria = False
cheque_especial = 450
saldo = 2000.0
saque = 2599

if conta_normal:
		if saldo >= saque:
			print("Saque realizado com sucesso!")
		elif saque <= (saldo + cheque_especial):
			print("Saque realizado com uso do cheque especial")
		else: 
			print("Não foi possível realizar o saque, saldo insuficiente")
elif conta_universitaria:
		if saldo >= saque:
			print("Saque realizado com sucesso")
		else: 
			print("Saldo insuficiente")
else:
	print("Sistema não reconheceu o tipo de conta, entre em contato com o seu gerente")