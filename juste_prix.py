from random import *

nombre_min = int(input("\nDonner une borne inférieur : "))
nombre_max = int(input("Donner une borne supérieur : "))
nombre = randint(nombre_min, nombre_max)
print("\nTrouvez un nombre entre {} et {} inclus.".format(nombre_min, nombre_max))
hypothese = int(input("Donnez votre nombre : "))

def juste_prix (prix, hypothese, nombre_min, nombre_max) :
    if nombre != hypothese :
        while prix != hypothese :
            if nombre > hypothese :
                print("Plus")
                hypothese = int(input("Donnez un nouveau nombre : "))
            else :
                print("Moins")
                hypothese = int(input("Donnez un nouveau nombre : "))
    
    return print("Vous avez trouvez le bon nombre !\n")

juste_prix(nombre, hypothese, nombre_min, nombre_max)