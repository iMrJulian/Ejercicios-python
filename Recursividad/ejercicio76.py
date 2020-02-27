def factorial(n):
	if n>0:
		return n*factorial(n-1)
	else:
		return 1

def ejercicio76():
	n = int(input("Ingrese el numero a calcular su factorial "))

	print(factorial(n))

ejercicio76()