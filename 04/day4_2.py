#!/usr/bin/python3

# Dia 4 parte 2
# See:  https://adventofcode.com/2023/day/4
# Date: 04/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Leer todas las líneas del fichero
lines = file.readlines()
sum = 0

print("La suma de partes es: " + str(sum))
file.close()
