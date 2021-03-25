from math import sqrt

n = int(input("numero: "))

def isPrime(x):
	for i in range(2,int(sqrt(x))):
		if n % i == 0:
			return False	
	return True

#if isPrime(n):
#	print("e' primo")
#	exit()

a = []
indice = 0
while n != 1:
	for i in range(2,n):
		if isPrime(i) and n % i == 0:
			#print("fattore\t\t: ",i) 
			print("{:10d}|".format(int(n)) + str(i)	)
			n = n/i
print(" "*9 + "1|1")
			
#	1, a^b, c^d, .. N
#		
#			123231|123
#			    23|234
			
