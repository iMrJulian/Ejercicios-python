import calculadora
def ejercicio81():
	numero1 = int(input("Ingrese el primer numero: "))
	numero2 = int(input("Ingrese el segundo numero: "))
	
	print(f"{numero1} + {numero2} = {calculadora.suma(numero1,numero2)} ")
	print(f"{numero1} - {numero2} = {calculadora.resta(numero1,numero2)} ")
	print(f"{numero1} * {numero2} = {calculadora.multiplicacion(numero1,numero2)} ")
	print(f"{numero1} / {numero2} = {calculadora.division(numero1,numero2)} ")
	print(f"{numero1} ^ {numero2} = {calculadora.potencia(numero1,numero2)} ")
