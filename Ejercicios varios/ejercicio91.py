
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