import calculadoraBin
def ejercicio83():
	numero1 = (input("Ingrese el primer numero en binario: "))
	numero2 = (input("Ingrese el segundo numero en binario: "))
	
	print(f"{numero1} + {numero2} = {bin(calculadoraBin.suma(numero1,numero2))} ")
	print(f"{numero1} - {numero2} = {bin(calculadoraBin.resta(numero1,numero2))} ")
	print(f"{numero1} * {numero2} = {bin(calculadoraBin.multiplicacion(numero1,numero2))} ")
	print(f"{numero1} / {numero2} = {bin(calculadoraBin.division(numero1,numero2))} ")

ejerciio83()