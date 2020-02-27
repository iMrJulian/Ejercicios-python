alto = int(input("ingrese el alto del rectangulo "))
ancho = int(input("ingrese el ancho del rectangulo "))

print(f"El area del rectangulo es: {alto*ancho}")
print(f"El perimetro del rectangulo es: {alto*2+ancho*2}")
print(f"La diagonal del rectangulo es: {((ancho**2)+(alto**2))**0.5}")