def countWords(string):
	count = 1 
	for i in string:
		if i == ' ':
			count += 1
	return count
	
print(countWords("ciao come stai?"))
