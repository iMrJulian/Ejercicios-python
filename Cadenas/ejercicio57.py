def ejercicio57():
	cadena = input("Ingrese una cadena: ")
	nMayusculas = 0

	for caracter in cadena:
		if caracter.isupper():
			nMayusculas +=1

	print(f"El numero de mayuscalas en la cadena es: {nMayusculas}")