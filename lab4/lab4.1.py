#Scrivete programmi che leggano una sequenza di numeri interi e visualizzino quanto
#segue:
#a. il valore minimo e il valore massimo tra quelli acquisiti
#b. il numero di valori pari e il numero di valori dispari tra quelli acquisiti;
#c. le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni
#nuova acquisizione (se, ad esempio, i valori in ingresso sono 1 7 2 9, il
#programma visualizzerà 1 8 10 19);
#d. i valori adiacenti duplicati (se, ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6
#6 6 3, il programma visualizzerà 3 5 6). [P4.2]

#caricamento numeri
n = 0
numeri = []
try:
	n = int(input("inserisci un numero: "))
except Exception:
	print("babbo, scrivi un numero!")
	exit()
	
while n != -1:
	numeri.append(n)
	
	try:
		 n = int(input("inserisci un numero: "))
	except Exception:
		print("babbo, scrivi un numero!")

print()

#val min e max
print("minimo\t:",min(numeri))
print("massimo\t:",max(numeri))

print()

#numero dispari e pari
pari = 0
for i in numeri:
	if i%2 == 0:
		pari +=1
print("pari\t:",pari)
print("dispari\t:",len(numeri)-pari)

print()

#somme parziali
print("somme parziali")
somma = 0
for i in numeri:
	somma += i
	print(somma,end=' ')


print("\n")

#valori adiacenti duplicati
print("valori adiacenti duplicati")

old = -1

for i in numeri:
	if old == i:
		print(i,end=' ')
	old = i

print()
