import math

#Ejercicios simples
def ejercicio4():
	alto = int(input("ingrese el alto del rectangulo "))
	ancho = int(input("ingrese el ancho del rectangulo "))
	
	print(f"El area del rectangulo es: {alto*ancho}")
	print(f"El perimetro del rectangulo es: {alto*2+ancho*2}")
	print(f"La diagonal del rectangulo es: {((ancho**2)+(alto**2))**0.5}")

def ejercicio14():
	x1 = int(input("ingrese x1"))
	y1 = int(input("ingrese y1"))
	x2 = int(input("ingrese x2"))
	y2 = int(input("ingrese y2"))

	print(f"El area del rectangulo es: {abs(x2-x1)*abs(y2-y1)}")

#Ejercios condicionales
def ejercicio18():
	n = int(input("ingrese el numero que quiere verificar: "))
	
	if(n%2):
		print("El numero es impar")
	else:
		print("El numero es par")

def ejercicio20():
	numero1 = int(input("Ingrese el primer numero: "))
	numero2 = int(input("Ingrese el segundo numero: "))
	
	if (numero2==(numero1**2)):
		print(f"{numero2} es cuadrado exacto de ({numero1})")
	elif (numero2>(numero1**2)):
		print(f"{numero2} es mayor al cuadrado de {numero1}")
	else:
		print(f"{numero2} es menor al cuadrado de {numero1}")

#Ejercicios con ciclos
def ejercicio29():
	for i in range(1,101):
		if i%5==0:
			print(i)

def ejercicio35():
	n = int(input("Ingrese el numero a calcular su factorial "))
	factorial = 1

	while True:
		factorial = factorial * n
		n = n - 1
		if n<=0:
			break

	print(factorial)

#Colecciones
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

def ejercicio43():
	lista = [x for x in range (41) if x%2==0]
	print(lista)
	sumatoria = 0

	for i in lista:
		sumatoria += i

	print(sumatoria)

#Cadena de caracteres
def ejercicio56():
	cadena = input("Ingrese una cadena: ")
	arrayCadena = cadena.split(" ")
	tCadena = ""

	for subCadena in arrayCadena:
		tCadena += subCadena

	print(tCadena)

def ejercicio57():
	cadena = input("Ingrese una cadena: ")
	nMayusculas = 0

	for caracter in cadena:
		if caracter.isupper():
			nMayusculas +=1

	print(f"El numero de mayuscalas en la cadena es: {nMayusculas}")

#Funciones y procedimientos
def distaciaDosPuntos(x1,y1,x2,y2):
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def ejercicio70():
	x1 = int(input("ingrese x1 "))
	y1 = int(input("ingrese y1 "))
	x2 = int(input("ingrese x2 "))
	y2 = int(input("ingrese y2 "))

	print(f"La distacia entre los dos puntos es: {distaciaDosPuntos(x1,y1,x2,y2)}")

def isNumero(caracter):
	return caracter.isdigit()

def ejercicio67():
	caracter = input("Ingrese un caracter: ")

	if(isNumero(caracter)):
		print(f"El caracter {caracter} es un numero")
	else:
		print(f"El caracter {caracter} no es un numero")

#Recursividad
def factorial(n):
	if n>0:
		return n*factorial(n-1)
	else:
		return 1

def ejercicio76():
	n = int(input("Ingrese el numero a calcular su factorial "))

	print(factorial(n))

def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

def ejercicio80():
	n = int(input("Ingrese el termino n que quiere hallar "))

	print(fibonacci(n))

#Modulos
import calculadora
def ejercicio81():
	numero1 = int(input("Ingrese el primer numero: "))
	numero2 = int(input("Ingrese el segundo numero: "))
	
	print(f"{numero1} + {numero2} = {calculadora.suma(numero1,numero2)} ")
	print(f"{numero1} - {numero2} = {calculadora.resta(numero1,numero2)} ")
	print(f"{numero1} * {numero2} = {calculadora.multiplicacion(numero1,numero2)} ")
	print(f"{numero1} / {numero2} = {calculadora.division(numero1,numero2)} ")
	print(f"{numero1} ^ {numero2} = {calculadora.potencia(numero1,numero2)} ")

import calculadoraBin
def ejercicio83():
	numero1 = (input("Ingrese el primer numero en binario: "))
	numero2 = (input("Ingrese el segundo numero en binario: "))
	
	print(f"{numero1} + {numero2} = {bin(calculadoraBin.suma(numero1,numero2))} ")
	print(f"{numero1} - {numero2} = {bin(calculadoraBin.resta(numero1,numero2))} ")
	print(f"{numero1} * {numero2} = {bin(calculadoraBin.multiplicacion(numero1,numero2))} ")
	print(f"{numero1} / {numero2} = {bin(calculadoraBin.division(numero1,numero2))} ")

#Archivos
import codecs
def ejercicio86():
	f = codecs.open ('tabla ascii.txt','w',"charmap")
	for i in range (33,255):
		f.write(chr(i))
	f.close()

def ejercicio87():
	f = codecs.open('tabla ascii.txt','r',"charmap")
	cadena = f.read()
	print(cadena)

#Ejercicios varios
def ejercicio90():
	hora = input("Ingerese la hora en hh:mm:ss: ").split(":")
	hhLimite = int(hora[0])
	mmLimite = int(hora[1])
	ssLimite = int(hora[2])
	hh = 0
	mm = 0
	ss = 0

	while(hhLimite!=hh or mmLimite!=mm or ssLimite!=ss):
		ss += 1
	
		if(ss == 60):
			mm += 1
			ss = 0
		
		if(mm == 60):
			hh += 1
			mm = 0
		
		if(hh == 13):
			hh = 1
	
		print(f"{hh}:{mm}:{ss}")

def ejercicio91():
	hora = input("Ingerese la hora en hh:mm:ss: ").split(":")
	hh = int(hora[0])
	mm = int(hora[1])
	ss = int(hora[2])

	while(0!=hh or 0!=mm or 0!=ss):
		ss += -1
	
		if(ss == -1):
			mm -= 1
			ss = 59
		
		if(mm == -1):
			hh -= 1
			mm = 59
		
		if(hh == 13):
			hh = 1
	
		print(f"{hh}:{mm}:{ss}")


ejercicio91()