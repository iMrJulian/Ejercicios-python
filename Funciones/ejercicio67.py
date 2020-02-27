def isNumero(caracter):
	return caracter.isdigit()

def ejercicio67():
	caracter = input("Ingrese un caracter: ")

	if(isNumero(caracter)):
		print(f"El caracter {caracter} es un numero")
	else:
		print(f"El caracter {caracter} no es un numero")

ejercicio67()