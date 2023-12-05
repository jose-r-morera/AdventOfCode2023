#!/usr/bin/python3

# Dia 5 parte 2
# See:  https://adventofcode.com/2023/day/5
# Date: 05/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Total
points_sum = 0

print("La suma de puntos es: " + str(points_sum))
file.close()
