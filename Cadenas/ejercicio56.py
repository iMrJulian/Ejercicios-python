def ejercicio56():
	cadena = input("Ingrese una cadena: ")
	arrayCadena = cadena.split(" ")
	tCadena = ""

	for subCadena in arrayCadena:
		tCadena += subCadena

	print(tCadena)

ejercicio56()