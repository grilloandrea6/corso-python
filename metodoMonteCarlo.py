from random import random

PROVE = 10**10
hits=0

for i in range(PROVE):
	r=random()
	x=-1+2*r
	r=random()
	y=-1+2*r

	if x**2 + y**2 <=1 :
		hits+=1
	
	if i % (PROVE/10) == 0:
		print ("sono arrivato al ",i/PROVE * 100,"%")

piEstimate = 4*hits/PROVE

print(piEstimate)
