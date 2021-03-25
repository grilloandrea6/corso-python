'''totale = 0F
inché la stringa s contenente il numero romano non è vuotaSe valore(primo carattere di s)è almeno uguale a v
alore(secondo carattere di s)oppure s ha lunghezza 1Aggiungi valore(primo carattere di s)a totale.

Elimina il primo carattere di s.AltrimentiAggiungi a totale la differenzavalore(secondo carattere di s)–valore(primo carattere di s)Elimina il primo e il secondo carattere di s'''

def valore(char):
	if char.upper() == "I":
		return 1
	
	if char.upper() == "V":
		return 5
	
	if char.upper() == "X":
		return 10
	
	if char.upper() == "L":
		return 50
	
	if char.upper() == "C":
		return 100
	
	if char.upper() == "D":
		return 500
	
	if char.upper() == "M":
		return 1000
	
	print("ERROR LETTER NOT RECOGNIZED")
	return -1
	
s = input("inserisci numero: ")
totale = 0


while s != '':
	if len(s) == 1 or valore(s[0]) >= valore(s[1]):
		totale += valore(s[0])
		s = s[1:]
	else:
		totale += (valore(s[0]) - valore(s[1]))
		s = s[2:]
		

print(totale)
