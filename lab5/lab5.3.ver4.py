n = int(input("numero: "))

i = 2

while n != 1:
	 
	while n % i == 0:
		print("{:30d}|{}".format(int(n),i) 	)
		n = n / i
			
	i += 1

print("{:30d}|1".format(int(n)))
