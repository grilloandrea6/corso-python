from sys import exit
NUMERO = 4155551212

nStringa = str(NUMERO)

if len(nStringa) != 10:
	exit("errore, il numero deve essere di 10 cifre")

print("(" + nStringa[:3] + ")" + nStringa[3:6] + "-" + nStringa[6:])
