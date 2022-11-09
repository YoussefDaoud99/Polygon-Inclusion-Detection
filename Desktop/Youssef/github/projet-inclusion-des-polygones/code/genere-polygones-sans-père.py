#!/usr/bin/env python3
import sys
"""
générateurs des polygones carrés sans père
"""

def main():
    #sys.argv[1] : le nom du fichier
    #sys.argv[2] : le nombre des polygones
    x, nombre_polygones = 0, int(sys.argv[2])
    with open(sys.argv[1], "w") as polygones:
        for i in range(nombre_polygones):
            polygones.write(str(i)+" "+str(x)+" "+str(x)+"\n"+str(i)+" "+str(x + 4)+" "+str(x)+"\n")
            polygones.write(str(i)+" "+str(x + 4)+" "+str(x + 4)+"\n"+str(i)+" "+str(x)+" "+str(x + 4)+"\n")
            x += 5

        


main()
