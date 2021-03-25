
stringa = input("inserisci una stringa: ")

print('\nmaiuscole')
for i in stringa:
	print( i if i.isupper() else '' ,end='')	

print('\n\nalternata')

for i in range(1,len(stringa),2):
	print(stringa[i],end='')

print('\n\nvocali sostituite con _')

for i in stringa:
	print( '_' if (i.lower() in {'a','e','i','o','u'}) else i, end='')
	
n_cifre = 0
for i in stringa:
			if i.isdigit():
					n_cifre += 1

print('\n\nnumero di cifre: ', n_cifre)

print('\nposizioni delle vocali')
for i in range(0,len(stringa)):
	print( (str(i)+' ') if (stringa[i] in {'a','e','i','o','u','A','E','I','O','U'}) else '', end='')
	
print('\n')
