from random import *

def coup_ordi(nombre) :
    if nombre == 1 :
        ordi = "pierre"
    elif nombre == 2 :
        ordi = "feuille"
    elif nombre == 3 :
        ordi = "ciseaux"
    else :
        print("Problème de conversion 2")
    return ordi
        
def coup_humain(choix) :
    nombre = 0
    if choix == "pierre" :
        nombre = 1
    elif choix == "feuille" :
        nombre = 2
    elif choix == "ciseaux" :
        nombre = 3
    else :
        print("Problème de conversion 1")
    return nombre

def gagnant(humain, ordi) :
    if humain == ordi :
        resultat = "égalité"
    elif humain - 1 == ordi or humain + 2 == ordi :
        resultat = "humain"
    else :
        resultat = "ordi"
    return resultat

def compteur(points_gagnant) :
    points_gagnant += 1
    return points_gagnant


print("\nLancement d'une partie de shifumi ...")
nombre_manches = int(input("Combien de manche pour gagner : "))
humain_points = 0
ordi_points = 0
while humain_points != nombre_manches and ordi_points != nombre_manches :
    nombre_ordi = randint(1, 3)
    choix = input("Quel coup voulez vous faire ?\t")
    # demande du choix
    print ("L'ordi fait {}.".format(coup_ordi(nombre_ordi)))
    nombre_humain = coup_humain(choix)
    #  conversion du choix en nombre
    resultat = gagnant(nombre_humain, nombre_ordi)
    if resultat == "humain" :
        humain_points = compteur(humain_points)
    elif resultat == "ordi" :
        ordi_points = compteur(ordi_points)
    # comptage des points
    print ("Humain = {} | Ordi = {}\n".format(humain_points, ordi_points))
print("Fin de la partie ...")
