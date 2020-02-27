def ejercicio35():
	n = int(input("Ingrese el numero a calcular su factorial "))
	factorial = 1

	while True:
		factorial = factorial * n
		n = n - 1
		if n<=0:
			break

	print(factorial)