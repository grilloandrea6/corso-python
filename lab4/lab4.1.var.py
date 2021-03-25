max = min = n = int(input("insert number: "))

pari = 0
dispari = 0

while n != '' :
	n=int(n)
	
	if n > max:
		max = n
	
	if n<min:
		min = n
	
	if n % 2 == 0:
		pari = pari + 1
	else:
		dispari +=1
	
	n = input("insert numer: ")

print ("numeri pari:",pari)
print ("numeri dispari:",dispari)
print ("max:",max)
print ("min:",min)	
