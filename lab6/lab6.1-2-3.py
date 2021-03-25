def countVowels(a):
	count = 0
	for i in a:
		if i.lower() in "aeiou":
			count += 1
	return count

print(countVowels("ciiaao"))	


def countWords(string):
	count = 1 
	for i in string:
		if i == ' ':
			count += 1
	return count
	
print(countWords("ciao come stai?"))


def find(string,match):
	return True if match in string else False
	
b = find("Mississippi", "sip")
print(b)	


