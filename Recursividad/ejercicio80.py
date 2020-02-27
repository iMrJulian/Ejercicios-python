def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

def ejercicio80():
	n = int(input("Ingrese el termino n que quiere hallar "))

	print(fibonacci(n))

ejercicio80()