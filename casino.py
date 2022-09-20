#!/usr/local/bin/python3.10

import random
import time
import os

argent = 100
r = 100
choix = 60
mise = 0
partir = False
is_choix_number = False
os.system("clear")

while partir==False :
	if argent == 0:
		print("Vous voulez quoi ??, Revenez quand vous aurez de la moula !!!")
		break
	else:
		print("Bienvenue :D !")

	time.sleep(1)
	mise = input("Vous misez combien?")

	if not mise.isnumeric():
		print("\t\nHein, quoi ?? On la refait.")
		time.sleep(1)
		os.system("clear")
		continue

	mise = int(mise)

	if mise > argent :
		print(f"\t\nHeu alors attendez, vous n'avez que {argent} euros la...")
		continue
	else:
		argent = argent - mise
		if mise <= 0:
			print("\t\nHey, il faut miser pour jouer ici.")
			time.sleep(1)
			continue
		print(f"\t\nOk vous avez misé {mise} euros, bonne chance!")
		print(f"\t\nIl vous reste {argent} euros")
		time.sleep(1)
	while True:
		choix = input("Choisissez un nombre entre 0 et 59 ou une couleur (noir ou rouge):")
		is_choix_number = choix.isnumeric()
		if is_choix_number == False:	
			if choix == "noir" or choix == "rouge" :
				print(f"\t\nVous avez choisi la couleur {choix}!")
				if choix == "noir":
					choix = 0
				else:
					choix = 1
				break
		else:
			choix = int(choix)
			if choix < 0 or choix > 59 :
				print("\t\nChoisissez un nombre entre 0 et 59 j'ai dit !")
				continue
			else:
				print(f"\t\nOk vous avez choisi {choix}!")
				time.sleep(1)
				break
	
	print("\t\nEt la roue tourne ! Les jeux sont faits !")
	time.sleep(1)
	print("\t\n.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)	
	r = random.randint(0,59)
	print(f"\t\nLa valeur est {r} ! Alors...")
	time.sleep(1)
	if is_choix_number == False :
		if r%2 == 0:
			print("\t\nPerdu !! haha ehehehehe")
		else:
			print("\t\nBrabo, c'est gagné.... hmm")
			argent = argent + mise*2			
	else :
		if choix == r :
			print("\t\nWwow... Bravo bravo... Tu remportes la mise.")
			argent = argent + mise*20
		else :
			print("\t\nHehehehe ahhh bah désolé mais c'est perdu on dirait :c")
			

	
	partir = input("\t\nOn continue ?? [y/n]")
	if partir == "y" :
		partir = False
	else:
		partir = True
print("========================")
print("=== FIN DE LA PARTIE ===")
print("========================")
