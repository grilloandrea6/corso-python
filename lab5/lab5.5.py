'''
In una simulazione predatore-preda, si calcolano le popolazioni di predatori (predators) e prede (preys) usando 
le equazioni seguenti:
	
	preyn+1 = preyn×(1 + A –B ×predn)
	
	predn+1 = predn×(1 –C + D ×preyn)
	
	In queste equazioni, A
 è il ritmo con cui le nascite di prede sovrastano le loro morti naturali, B è il ritmo di predazione, C è il 
 ritmo con cui le morti di predatori sovrastano le nascite in caso di assenza di cibo e D è il ritmo con cui 
 aumentano i predatori in presenza di cibo.Scrivete un programma che chieda questi valori all’utente, oltre 
 alle dimensioni iniziali delle popolazioni e al numero di intervalli di tempo che coinvolgono la simulazione.
  Successivamente, il programma deve visualizzare la dimensione delle due popolazioni per il numero di intervalli
   di tempo assegnato. Eseguite, come esempio, una simulazione con A = 0.1, B = C = 0.01 e D = 0.00002, con popolazione
    iniziale di 1000 prede e 20 predatori. '''

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
D = float(input("D = "))

preys = int(input("predeIniziali = "))
predators = int(input("predatoriIniziali = "))
dt = int(input("numero intervalli di tempo = "))

for i in range(dt):
	print ( "prede\t",int(preys))
	print("predatori\t",int(predators))
	
	newPreys = preys*(1 + A - B * predators)
	predators = predators * ( 1 - C + D * preys)
	preys = newPreys

	
