import math

def addition_vecteur(vecteur1: list, vecteur2: list):

    return [vecteur1[0]+vecteur2[0],vecteur1[1]+vecteur2[1]]

def get_direction(angle: float):
    
    return [math.cos(angle), math.sin(angle)]

def get_norme(vecteur: list):

    return math.sqrt(vecteur[0]*vecteur[0]+vecteur[1]*vecteur[1])

def get_vecteur_with_angle(angle: float, norme: int):

    return [ norme * math.cos(angle), norme * math.sin(angle)]

