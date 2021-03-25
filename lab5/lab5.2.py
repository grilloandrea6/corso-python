'''pin = 1234

for i in range(3):
	if(int(input("insert pin: ")) == pin):
		print("correct pin")
		exit()
	else:
		print("error!")

print("your bank card is blocked!")
'''

#TODO
pin = 1234
correct = False
i = 0
while i < 3:
	attempt = input("insert  pin: ")
	if len(attempt) == 4 and attempt.isdigit():
		
	
	if not correct:
		if(int(input("insert pin: ")) == pin):
			print("correct pin")
			correct = True
		else:
			print("error!")

if not correct:
	print("your bank card is blocked!")


