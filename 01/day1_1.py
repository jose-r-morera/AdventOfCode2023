#!/usr/bin/python3

# Dia 1 parte 1
# See:  https://adventofcode.com/2023/day/1
# Date: 01/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

sum = 0
for line in file:
  digits = re.findall(r'\d', line)
  sum += int(digits[0]+digits[-1])


print("La suma es: " + str(sum))
file.close()