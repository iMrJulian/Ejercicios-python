def distaciaDosPuntos(x1,y1,x2,y2):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def ejercicio70():
	x1 = int(input("ingrese x1 "))
	y1 = int(input("ingrese y1 "))
	x2 = int(input("ingrese x2 "))
	y2 = int(input("ingrese y2 "))

	print(f"La distacia entre los dos puntos es: {distaciaDosPuntos(x1,y1,x2,y2)}")

ejercicio70()