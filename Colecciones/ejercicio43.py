def ejercicio43():
	lista = [x for x in range (41) if x%2==0]
	print(lista)
	sumatoria = 0

	for i in lista:
		sumatoria += i

	print(sumatoria)

ejercicio43()