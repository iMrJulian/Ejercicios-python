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

ejercicio90()