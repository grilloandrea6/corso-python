a = 32310901
b = 1729
m = 2**24

r = float(input("inserisci il seed: "))

for i in range(100):
	r = int((a * r + b) % m)
	
	print(f"numero generato: {r}")
