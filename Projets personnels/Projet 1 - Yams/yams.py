import numpy


# Initialisation_________________________________________________________________________________________________________________________________________________________

# Initialise le score des joueurs à 0 dans chaque case
def initialisation_joueurs(nombre_joueurs):

	liste_joueurs = []
	for _ in range(nombre_joueurs) :
		score_joueur = {"un": None, "deux" : None, "trois" : None, "quatre" : None, "cinq" : None, "six" : None, "brelan": None,
		"full" : None, "carre": None, "p_suite" : None, "g_suite" : None, "yams" : None, "chance" : None}
		liste_joueurs.append(score_joueur)
	return liste_joueurs


def nomme_les_joueurs(nombre_joueurs) :
	liste_noms = []
	for i in range(nombre_joueurs) :
		print(f"Joueur {i+1}, quel est ton nom ?")
		nom = input()
		liste_noms.append(nom)
	return liste_noms



#Décris les règles du jeu
def description_regle() :
	print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("Le jeu du Yams consiste à chaque tour à lancer 5 dés pour faire des combinaisons pour remplir une grille de valeur. Le joueur avec le plus grand score gagne.")
	print("A chaque tour il est possible de relancer les dés que l'on souhaite 2 fois.")
	print("Une case de la grille ne peut être remplie qu'une seule fois, voici la grille avec les scores que cela donne :")
	print("un            |  Total des 1")
	print("------------------------------")
	print("deux          |  Total des 2")
	print("------------------------------")
	print("trois         |  Total des 3")
	print("------------------------------")
	print("quatre        |  Total des 4")
	print("------------------------------")
	print("cinq          |  Total des 5")
	print("------------------------------")
	print("six           |  Total des 6")
	print("------------------------------")
	print("brelan        |  Total des 3 dés")
	print("------------------------------")
	print("full          |  25 points")
	print("------------------------------")
	print("carré         |  Total des 4 dés")
	print("------------------------------")
	print("petite suite  |  30 points")
	print("------------------------------")
	print("grande suite  |  40 points")
	print("------------------------------")
	print("yams          |  50 points")
	print("------------------------------")
	print("chance        |  Total des 5 dés")

# Vérifications des input_________________________________________________________________________________________________________________________________________________________________

def verification_des(resultat_des_physiques) :
	valeur_possibles = ["1", "2", "3", "4", "5", "6"]
	while True :
		if len(resultat_des_physiques) != 5 :
			print("Il faut entrer les cinq valeurs des dés, veuillez réessayer :")
			resultat_des_physiques = input()
		else :
			for i in (resultat_des_physiques) :
				if i not in valeur_possibles :
					print(f"Un dés ne peut faire la valeur {i}, veuillez réessayer")
					resultat_des_physiques = input()
					break
			else : return resultat_des_physiques


def verification_oui_ou_non(mot) :
	mot = mot.lower()
	while mot not in ("oui", "non") :
		mot = input("Ce n'est pas la réponse attendu, réponds par oui ou par non :")
		mot = mot.lower()
	return mot

def verification_relance() :
    relance_possible = ["1", "2", "3", "4", "5"]
    while True:
        print("Quels dés veux-tu relancer ? Note les numéros des dés que tu veux relancer de 1 à 5")
        nombre_input = input()
        for i in nombre_input :
            if i not in relance_possible :
                print(f"Il n'y a pas de dés numéro {i}")
                break
        else:
            return nombre_input

def verification_nombre_joueur() :
	while True:
		print("Combien de joueur êtes-vous ?")
		nombre_joueurs = input()
		try :
			nombre_joueurs = int(nombre_joueurs)
		except : ValueError
		if type(nombre_joueurs) != int or nombre_joueurs <= 0 :
			print("Ce n'est pas un nombre de joueurs possible")
		else :
			return nombre_joueurs



# Affichage_______________________________________________________________________________________________________________________________________________________________________________

def affichage_score(score, numero_joueur) :
	for i in (score[numero_joueur]):
		if score[numero_joueur][i] == None :
			score[numero_joueur][i] = "Vide"

	print("")
	print(f"un            |  {score[numero_joueur]["un"]}")
	print(f"------------------------------")
	print(f"deux          |  {score[numero_joueur]["deux"]}")
	print(f"------------------------------")
	print(f"trois         |  {score[numero_joueur]["trois"]}")
	print(f"------------------------------")
	print(f"quatre        |  {score[numero_joueur]["quatre"]}")
	print(f"------------------------------")
	print(f"cinq          |  {score[numero_joueur]["cinq"]}")
	print(f"------------------------------")
	print(f"six           |  {score[numero_joueur]["six"]}")
	print(f"------------------------------")
	print(f"brelan        |  {score[numero_joueur]["brelan"]}")
	print(f"------------------------------")
	print(f"full          |  {score[numero_joueur]["full"]}")
	print(f"------------------------------")
	print(f"carré         |  {score[numero_joueur]["carre"]}")
	print(f"------------------------------")
	print(f"petite suite  |  {score[numero_joueur]["p_suite"]}")
	print(f"------------------------------")
	print(f"grande suite  |  {score[numero_joueur]["g_suite"]}")
	print(f"------------------------------")
	print(f"yams          |  {score[numero_joueur]["yams"]}")
	print(f"------------------------------")
	print(f"chance        |  {score[numero_joueur]["chance"]}")
	print(f"------------------------------")
	print("")

	for i in (score[numero_joueur]) :
		if score[numero_joueur][i] == "Vide" :
			score[numero_joueur][i] = None


# Lancer les dés___________________________________________________________________________________________________________________________________________________________________________

#lance les dés en random
def random_des(nombre_relance) :
	resultat_des = []
	for i in range (nombre_relance) :
		resultat_des.append(random_valeur_des())

	return (resultat_des)

#relance certains dés en random
def random_valeur_des() :
	valeur_des = numpy.random.randint(1, 7)
	return valeur_des


#lance les dés pendant un tour en appelant les fonctions random
def lancer_les_des(numero_joueur, liste_noms) :
	de1 = 0
	de2 = 0
	de3 = 0
	de4 = 0
	de5 = 0

	print("-----------------------------------------------------------------------------------------------------------------------------------------------")
	print(f"{liste_noms[numero_joueur]}, c'est à toi de jouer, voici ta grille de score :")
	affichage_score(score, numero_joueur)
	print("Tape entrée pour lancer les dés !")
	input()
	resultat_des = random_des(5)
	print(resultat_des)
	continuer = input("Veux-tu relancer des dés ? Tape oui ou non :")
	continuer = verification_oui_ou_non(continuer)
	if continuer == "oui" :
		nombres_des_relance1 = verification_relance()
		liste_des_relance1 = []
		for i in range (len((nombres_des_relance1))) :
			liste_des_relance1.append(int(nombres_des_relance1[i])-1)
		for i in liste_des_relance1 :
			resultat_des[i] = random_valeur_des()
		print(resultat_des)
		continuer = input("Veux-tu relancer des dés ? Tape oui ou non :")
		continuer = verification_oui_ou_non(continuer)
		if continuer == "oui" :
			nombres_des_relance2 = verification_relance()
			liste_des_relance2 = []
			for i in range (len(nombres_des_relance2)) :
				liste_des_relance2.append(int(nombres_des_relance2[i])-1)
			for i in liste_des_relance2 :
				resultat_des[i] = random_valeur_des()
			print(resultat_des)
	input("Clique sur entrée pour affecter ton résultat")

	return resultat_des


# affectation _____________________________________________________________________________________________________________________________________________________________________________________
#fait le choix d'affection du score dans les cases


def affectation(resultat_des, numero_joueur, score) :
	print("Quelle case choisissez-vous ?")
	choix = input("Choisissez la case :")
	choix = choix.lower()
	if choix == "petite suite" :
		choix = "p_suite"
	if choix == "grande suite" :
		choix = "g_suite"
	if choix == "carré" :
		choix = "carre"
	choix_possible = ["un","deux","trois","quatre","cinq","six","brelan","full","p_suite","g_suite","carre","yams","chance"]
	if choix in choix_possible :

		if score[numero_joueur][choix] != None :
			print(f"La case {choix} est déjà affectée !")
			input("CLique sur entrer pour choisir une autre case")
			affectation(resultat_des, numero_joueur, score)

		else :
			match choix :
				case "un" :
					valeur_un = affectation_un(resultat_des, numero_joueur, score)
					if valeur_un != None :
						score[numero_joueur]["un"] = valeur_un
				case "deux" :
					valeur_deux = affectation_deux(resultat_des, numero_joueur, score)
					if valeur_deux != None :
						score[numero_joueur]["deux"] = valeur_deux
				case "trois" :
					valeur_trois = affectation_trois(resultat_des, numero_joueur, score)
					if valeur_trois != None :
						score[numero_joueur]["trois"] = valeur_trois
				case "quatre" :
					valeur_quatre = affectation_quatre(resultat_des, numero_joueur, score)
					if valeur_quatre != None :
						score[numero_joueur]["quatre"] = valeur_quatre
				case "cinq" :
					valeur_cinq = affectation_cinq(resultat_des, numero_joueur, score)
					if valeur_cinq != None :
						score[numero_joueur]["cinq"] = valeur_cinq
				case "six" :
					valeur_six = affectation_six(resultat_des, numero_joueur, score)
					if valeur_six != None :
						score[numero_joueur]["six"] = valeur_six
				case "brelan" :
					valeur_brelan = affectation_brelan(resultat_des, numero_joueur, score)
					if valeur_brelan != None :
						score[numero_joueur]["brelan"] = valeur_brelan
				case "full" :
					valeur_full = affectation_full(resultat_des, numero_joueur, score)
					if valeur_full != None :
						score[numero_joueur]["full"] = valeur_full
				case "carre" :
					valeur_carre = affectation_carre(resultat_des, numero_joueur, score)
					if valeur_carre != None :
						score[numero_joueur]["carre"] = valeur_carre
				case "p_suite" :
					valeur_p_suite = affectation_p_suite(resultat_des, numero_joueur, score)
					if valeur_p_suite != None :
						score[numero_joueur]["p_suite"] = valeur_p_suite
				case "g_suite" :
					valeur_g_suite = affectation_g_suite(resultat_des, numero_joueur, score)
					if valeur_g_suite != None :
						score[numero_joueur]["g_suite"] = valeur_g_suite
				case "yams" :
					valeur_yams = affectation_yams(resultat_des, numero_joueur, score)
					if valeur_yams != None :
						score[numero_joueur]["yams"] = valeur_yams
				case "chance" :
					valeur_chance = affectation_chance(resultat_des, numero_joueur, score)
					if valeur_chance != None :
						score[numero_joueur]["chance"] = valeur_chance
	else :
		print(f"La case {choix} n'existe pas.")
		input("Clique sur Entrer pour choisir une autre case")
		affectation(resultat_des, numero_joueur, score)



def affectation_un(resultat_des, numero_joueur, score) :

		valeur = resultat_des.count(1)
		print(f"Es-tu sûr de vouloir mettre la valeur {valeur} au 1 ?")
		choix = input()
		choix = verification_oui_ou_non(choix)
		if choix == "oui" :
			return valeur
		else :
		 	affectation(resultat_des, numero_joueur, score)


def affectation_deux(resultat_des, numero_joueur, score) :

	valeur = resultat_des.count(2)
	valeur_final = valeur*2
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au 2 ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_trois(resultat_des, numero_joueur, score) :
	valeur = resultat_des.count(3)
	valeur_final = valeur*3
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au 3 ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_quatre(resultat_des, numero_joueur, score) :
	valeur = resultat_des.count(4)
	valeur_final = valeur*4
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au 4 ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_cinq(resultat_des, numero_joueur, score) :
	valeur = resultat_des.count(5)
	valeur_final = valeur*5
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au 5 ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_six(resultat_des, numero_joueur, score) :
	valeur = resultat_des.count(6)
	valeur_final = valeur*6
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au 6 ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_brelan(resultat_des, numero_joueur, score) :
	valeur_final = 0
	for i in range(1, 7) :
		if resultat_des.count(i) > 2 :
			valeur_final = i*3
			break
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au brelan ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)


def affectation_full(resultat_des, numero_joueur, score) :
	nombre_de_fois = []
	for i in range(1, 7) :
		nombre_de_fois.append(resultat_des.count(i))
	if 2 in nombre_de_fois and 3 in nombre_de_fois :
		valeur_final = 25
	else :
		valeur_final = 0
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au full ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_carre(resultat_des, numero_joueur, score) :
	valeur_final = 0
	for i in range(1,7) :
		if resultat_des.count(i) > 3 :
			valeur_final = i*4
			break
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au carré ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_p_suite(resultat_des, numero_joueur, score) :
	resultat_des.sort()
	liste_des_p_suite_possible = ([1, 1, 2, 3, 4], [1, 2, 2, 3, 4], [1, 2, 3, 3, 4], [1, 2, 3, 4, 4], [1, 2, 3, 4, 5],[1, 2, 3, 4, 6],
	 [1, 2, 3, 4, 5], [2, 2, 3, 4, 5], [2, 3, 3, 4, 5], [2, 3, 4, 4, 5], [2, 3, 4, 5, 5], [2, 3, 4, 5, 6],
	 [1, 3, 4, 5, 6], [2, 3, 4, 5, 6], [3, 3, 4, 5, 6], [3, 4, 4, 5, 6], [3, 4, 5, 5, 6], [3, 4, 5, 6, 6])

	if resultat_des in liste_des_p_suite_possible :
		valeur_final = 30
	else :
		valeur_final = 0
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} à la petite suite ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_g_suite(resultat_des, numero_joueur, score) :
	if 2 in resultat_des and 3 in resultat_des and 4 in resultat_des and 5 in resultat_des and (1 in resultat_des or 6 in resultat_des) :
		valeur_final = 40
	else :
		valeur_final = 0
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} à la grande suite ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_yams (resultat_des, numero_joueur, score) :
	valeur_final = 0
	for i in range(1 ,7) :
		if 5 == resultat_des.count(i) :
			valeur_final = 50
			break
	print(f"Es-tu sûr de vouloir mettre la valeur {valeur_final} au Yams ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return valeur_final
	else :
		affectation(resultat_des, numero_joueur, score)

def affectation_chance(resultat_des, numero_joueur, score) :
	somme = 0
	for des in resultat_des :
		somme += des
	print(f"Es-tu sûr de vouloir mettre la valeur {somme} à la chance ?")
	choix = input()
	choix = verification_oui_ou_non(choix)
	if choix == "oui" :
		return somme
	else :
		affectation(resultat_des, numero_joueur, score)


# Ordre des tours_________________________________________________________________________________________________________________________________________________________________________

def ordre_tours() :

	for _ in range(13) :
		for numero_joueur in range(len(score)) :
			resultat_des = lancer_les_des(numero_joueur, liste_noms)
			affectation(resultat_des, numero_joueur, score)

def ordre_tours_avec_des() :

	for _ in range(13) :
		for numero_joueur in range(len(score)) :
			print(f"{liste_noms[numero_joueur]}, c'est à toi de jouer, voici ta grille de score :")
			affichage_score(score, numero_joueur)
			resultat_des = []
			resultat_des_physiques = input("Entrer vos réultats aux dés, tout attachés :")
			resultat_des_physiques = verification_des(resultat_des_physiques)
			for i in range(len(resultat_des_physiques)) :
				resultat_des.append(int(resultat_des_physiques[i]))
			print(resultat_des)
			affectation(resultat_des, numero_joueur, score)
# Victoire_________________________________________________________________________________________________________________________________________________________________________________

def victoire(score, liste_noms) :

	liste_total = []

	for i in range(len(score)) :
		somme = 0
		for y in (score[i]) :
			somme += score[i][y]
		liste_total.append(somme)

	for i in range(len(liste_noms)) :
		print(f"{liste_noms[i]}, tu as marqué {liste_total[i]} points !")

	liste_gagnant = []

	for i in range(len(liste_noms)) :
		if liste_total[i] == max(liste_total) :
			liste_gagnant.append(liste_noms[i])
	if len(liste_gagnant) == 1 :
		print(f"Félicitations {liste_gagnant[0]}, tu as gagné !")
	else :
			print(f"Félicitations {liste_gagnant}, vous êtes gagnants à égalité !")




#________________________________Main__________________________________________________________________________________________________________________________________________________________
if __name__ == "__main__" :

	print("Bienvenue dans le jeu du Yams, souhaitez-vous voir les règles du jeu ?")
	regle =  input("Réponds pas oui ou par non :")
	regle = verification_oui_ou_non(regle)
	if regle == "oui" :
		description_regle()

	print("Possédez-vous des dés physiques ?")
	des_physiques = input("Réponds par oui ou par non :")
	des_physiques = verification_oui_ou_non(des_physiques)

	nombre_joueurs = verification_nombre_joueur()

	score = initialisation_joueurs(nombre_joueurs)

	liste_noms = nomme_les_joueurs(nombre_joueurs)

	if des_physiques == "oui" :

		ordre_tours_avec_des()

	else :

		ordre_tours()

	victoire(score, liste_noms)











