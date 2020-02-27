import codecs
def ejercicio86():
	f = codecs.open ('tabla ascii.txt','w',"charmap")
	for i in range (33,255):
		f.write(chr(i))
	f.close()

ejercicio86()