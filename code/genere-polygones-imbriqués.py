#!/usr/bin/env python3
import sys
"""
générateurs des polygones carrés imbriqués
"""

def main():
    #sys.argv[1] : le nom du fichier
    #sys.argv[2] : le nombre des polygones
    x, nombre_polygones = 0, int(sys.argv[2])
    with open(sys.argv[1], "w") as polygones:
        j = 0
        for i in range(nombre_polygones):
            polygones.write(str(i)+" "+str(x - j)+" "+str(x - j)+"\n"+str(i)+" "+str(x - j)+" "+str(x + 4 + j)+"\n")
            polygones.write(str(i)+" "+str(x + 4 + j )+" "+str(x + 4 + j)+"\n"+str(i)+" "+str(x + 4 + j)+" "+str(x - j)+"\n")
            j += 1

main()
