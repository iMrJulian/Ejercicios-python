def ejercicio41():
	vocales = ("a","e","i","o","u")
	consonantes = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
	cadena = input("ingrese una cadena de caracteres")
	nVocales = 0
	nConsonantes = 0
	ninguno = 0

	for caracter in cadena:
		if caracter in vocales:
			nVocales += 1
		elif caracter in consonantes:
			nConsonantes += 1
		else:
			ninguno +=1

	print(f"El numero de vocales es: {nVocales}")
	print(f"El numero de consonates es: {nConsonantes}")
	print(f"El numero de caracteres distintos es: {ninguno}")

ejercicio41()