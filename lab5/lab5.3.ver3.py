from math import sqrt

n = int(input("numero: "))

original = n

i = 2

esponente = 0


print("1",end='')

while n != 1:
	 
	while n % i == 0:
		n = n / i
		esponente += 1
	
	if esponente == 1 :
		print(', ' +str(i), end='')	
	elif esponente > 0 :
		print(', ' + str(i) + "^" + str(esponente),end='')
	
	
	esponente = 0
	i += 1

print(', ' + str(original) )
'''		
			print("{:10d}|".format(int(n)) + str(i)	)
			n = n/i
print(" "*9 + "1|1")'''
			
#	1, a^b, c^d, .. N
#		
#			123231|123
#			    23|234
			
