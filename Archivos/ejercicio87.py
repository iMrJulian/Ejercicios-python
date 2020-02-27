import codecs
def ejercicio87():
	f = codecs.open('tabla ascii.txt','r',"charmap")
	cadena = f.read()
	print(cadena)

ejercicio87()