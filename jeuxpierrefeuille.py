import random

def jeux_devinette():
	action = True
	while action:
		mot_possible = ['Pierre', 'Papier', 'Ciseaux']
		mot_a_deviner = random.choice(mot_possible)

		print("Bienvenue dans le jeux jeux_devinette! \n L'ordinateur a choisie Entre Pierre, Papier, Ciseaux \n maintenant a vous de choisir")
		choix = str(input("Choisissez Pierre, Papier , Ciseaux: "))

		if mot_a_deviner == "Pierre" and choix == "Pierre":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Partie Nulle")
		elif mot_a_deviner == "Ciseaux" and choix == "Ciseaux":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Partie Nulle")
		elif mot_a_deviner == "Papier" and choix == "Papier":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Partie Nulle")

		elif mot_a_deviner == "Pierre" and choix == "Papier":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Vous avez gagne contre l'ordi")
		elif mot_a_deviner == "Papier" and choix == "Pierre":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("L'ordinateur a gagne")

		elif mot_a_deviner == "Pierre" and choix == "Ciseaux":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("L'ordinateur a gagne")
		elif mot_a_deviner == "Ciseaux" and choix == "Pierre":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Vous avez gagne contre l'ordi")

		elif mot_a_deviner == "Papier" and choix == "Ciseaux":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("Vous avez gagne contre l'ordi")
		elif mot_a_deviner == "Ciseaux" and choix == "Papier":
			print(f"L'ordinateur a choissi {mot_a_deviner} et vous avez choissi {choix}")
			print("L'ordinateur a gagne")
		else:
			print("Wrong")

		question = input("Aimeriez vous continuer? Oui ------> Continuer / Non --------------> Stop: ")

		if question == "Non" or question == "non" or question == "NON":
			action = False
			print("Merci d'avoir participer au jeux de devinette ! ! ! ")
		elif question == "Oui" or question == "oui":
			pass

jeux_devinette()