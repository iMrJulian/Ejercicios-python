def ejercicio20():
	numero1 = int(input("Ingrese el primer numero: "))
	numero2 = int(input("Ingrese el segundo numero: "))
	
	if (numero2==(numero1**2)):
		print(f"{numero2} es cuadrado exacto de ({numero1})")
	elif (numero2>(numero1**2)):
		print(f"{numero2} es mayor al cuadrado de {numero1}")
	else:
		print(f"{numero2} es menor al cuadrado de {numero1}")