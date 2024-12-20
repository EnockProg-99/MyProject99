import random

def jeux_mathematique():
	action = True
	nom = input("Entrer votre nom: ")
	print(f"Bonjour {nom}, Bienvenue dans le jeux de calcule mathematique")
	bonne_reponse = 0
	while action:
		nombre1 = random.randint(1,10)
		nombre2 = random.randint(1,10)

		operateur_calcule = ['+','*']
		choix_operateur = random.choice(operateur_calcule)

		questions = f"{nombre1} {choix_operateur} {nombre2}"
		print(f" Quelle est la reponse de {questions} ?")
		respons_correct = input("Entrer la bonne response: ")
		if choix_operateur == '+':
			bonne_reponse = nombre1+nombre2
			print(f"La bonne reponse est: {bonne_reponse}")
			if bonne_reponse == respons_correct:
				print("Bonne Response")
			else:
				print("Mauvaise response")
		elif choix_operateur == '*':
			bonne_reponse = nombre1*nombre2
			print(f"La bonne reponse est: {bonne_reponse}")
			if bonne_reponse ==:
				print("Mauvaise Response")
				
			else:
				print("Bonne response!")
		else:
			print("Wrong")

				

		question = input("Aimeriez vous continuer? Oui ------> Continuer / Non --------------> Stop: ")

		if question == "Non" or question == "non" or question == "NON":
			action = False
			print("Merci d'avoir participer au jeux de devinette ! ! ! ")
		elif question == "Oui" or question == "oui":
			pass

jeux_mathematique()