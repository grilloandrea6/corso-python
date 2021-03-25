
def calcolaInteresse(iniziale, interesse, nAnni):
	if nAnni == 0:
		return iniziale
	return calcolaInteresse(iniziale*(interesse + 1),interesse, nAnni - 1)


print(calcolaInteresse(100,0.05,20))

