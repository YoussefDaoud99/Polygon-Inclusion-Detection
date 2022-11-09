#!/usr/bin/env python3

import time
from geo.polygon import Polygon
from geo.point import Point
from geo.segment import Segment
import sys
from tycat import read_instance

def fusion(polygones ,inf ,sup ,moyenne):
    copie_polygones = []
    if inf < sup :
        #i indice de parcours de la liste de gauche
        #j indice de parcours de la liste de droite
        i , j = inf , moyenne + 1
        #il reste des termes dans les deux listes
        while i <= moyenne and j <= sup :
            #choix du terme à copier
            #polygones[i][2] est est la valeur absolue de la surface du i-ème polygone
            if polygones[i][2] <= polygones[j][2] :
                copie_polygones.append(polygones[i])
                i += 1
            else:
                copie_polygones.append(polygones[j])
                j += 1
        #si liste de gauche épuisée, on complète par liste de droite
        if i > moyenne:
            for t in range (j , sup + 1) :
                copie_polygones.append(polygones[t])
        #si liste de droite épuisée, on complète par liste de gauche
        if j > sup:
            for t in range (i ,moyenne + 1) :
                copie_polygones.append(polygones[t])
        #on réaffecte la liste L (effet de bord)
        for k in range (inf , sup + 1) :
            polygones[k] = copie_polygones[k - inf]


def triFusion(polygones, inf, sup):
    """
    On tri la liste des polygones selon la surface
    """
    if inf < sup:
        moyenne = (inf + sup) // 2
        triFusion(polygones, inf, moyenne)
        triFusion(polygones ,moyenne + 1 ,sup)
        fusion(polygones, inf, sup, moyenne)

def wn_est_dans(point,polygon):
    """ renvoie si le point est dans un polygone donné """
    ab = point.coordinates[0]
    wn =0
    for seg in polygon.segments():
        p1, p2 = seg.endpoints[0], seg.endpoints[1]
        x1 , x2= p1.coordinates[0], p2.coordinates[0]
        P = Polygon([p1,p2,point])
        if ab < x1:
            if ab >= x2:
                if  P.is_oriented_clockwise():
                    wn +=1
        else:
            if ab < x2:
                if not P.is_oriented_clockwise():
                    wn -=1
    return wn


def est_inclus(poly1, poly2):
    """ renvoie si le poly1 est dans un poly2 """
    if wn_est_dans(poly1.points[0], poly2):
        return True
    return False

def trouve_inclusions(polygones):
    """
    renvoie le vecteur des inclusions
    la ieme case contient l'indice du polygone
    contenant le ieme polygone (-1 si aucun).
    (voir le sujet pour plus d'info)
    """
    taille = len(polygones)
    liste = []
    tab = [-1]*taille #On initialise le vecteur des inclusions par des -1
    #On remplit liste par les triplets de (polygone, son numéro, la valeur absolue de sa surface) 
    for indice, poly in enumerate(polygones):
        liste.append((poly, indice,  abs(poly.area())))
    triFusion(liste, 0, taille - 1) #On trie liste par rapport à abs(poly.area())
    for i in range(taille - 1):
        j = i+1
        #La deuxième condition : teste si on n'a pas encore trouvé le père du polygone i.
        while j < taille and tab[liste[i][1]] == -1:
            if est_inclus(liste[i][0], liste[j][0]):
                #On met à l'indice du poly i le numéro du poly j père qu'est son père
                tab[liste[i][1]] = liste[j][1]
            j += 1
               
    return tab
    
def main():
    """
    charge chaque fichier .poly donne
    trouve les inclusions
    affiche l'arbre en format texte
    """
    for fichier in sys.argv[1:]:
        polygones = read_instance(fichier)
        inclusions = trouve_inclusions(polygones)
        print(inclusions)
if __name__ == "__main__":
    main()
