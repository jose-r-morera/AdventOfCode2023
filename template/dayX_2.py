#!/usr/bin/python3

# Dia X parte 2
# See:  https://adventofcode.com/2023/day/X
# Date: XX/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

points_sum = 0 # Total

print("La suma de puntos es: " + str(points_sum))
file.close()
