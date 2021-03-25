exceptionsLe = { "belize","Cambodge","Mexique•","Mozambique","Zaïre","Zimbabwe"}
exceptionsLes = {"etats-unis","pays-bas"}
vocali = {"a","e","i","o","u"}


nome = input("inserisci nome paese: ")

if nome.lower() in exceptionsLe:
	print("Le",nome)
elif nome.lower() in exceptionsLes:
	print("Les",nome)
elif nome[0].lower() in vocali:
	print("L'"+nome)
elif nome[-1].lower() == 'e':
	print("La",nome)
else:
	print("Le",nome)




