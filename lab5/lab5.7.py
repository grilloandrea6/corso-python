nBiglietti = 100
maxVendita = 4

while nBiglietti > 0:
	n = int(input("quanti biglietti vuoi acquistare?"))
	
	if (0 < n <= maxVendita) and (n <= nBiglietti):
		nBiglietti -= n
		print(f"venduti {n} biglietti")
	else:
		print("numero non valido")
	
	print(f"rimangono {nBiglietti}")
	
