lato = int(input("inserisci lato: "))

for i in range(lato):
	print('*'*lato)

print("\n\n")

for i in range(1, lato * 2, 2):
	print(' ' * round((lato * 1.99 - i) / 2), end = '')
		
	print('*' * i)


for i in range((lato * 2) - 3, 0, -2):
	print(' ' * round((lato * 1.99 - i) / 2), end = '')
	
	print('*' * i)
