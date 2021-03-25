a = (input("1: "),input("2: "),input("3: "))

for i in sorted(a):
	print(i)
	
s1 = a[0]
s2 = a[1]
s3 = a[2]

print()
print()

if s1 < s2:
	if s1 < s3:
		print(s1)
		if s2 < s3:
			print(s2)
			print(s3)
		else:
			print(s3)
			print(s2)
	else:
		print(s3)
		print(s1)
		print(s2)
else: # s2 < s1
	if s2 < s3:
		print(s2)
		
		if(s1 < s3):
			print(s1)
			print(s3)
		else:
			print(s3)
			print(s1)
	else:
		print(s3)
		print(s1)
		print(s2)
	
	'''
	if s1 < s3:
		print(s2)
		print(s1)
		print(s3)
	else: # s1 > s2 && s1 > s3
		if s2 < s3:
			print(s2)
			print(s3)
		else:
			print(s3)
			print(s2)
			
		print(s1)
'''
