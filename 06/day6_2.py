#!/usr/bin/python3

# Dia 6 parte 2
# See:  https://adventofcode.com/2023/day/6
# Date: 06/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

result = 0 # Formas de ganar la carrera
race = [0,0] # Carrera formada por [tiempo, distancia]

for i in [0, 1]:
  accumulator = ""
  for partial_value in re.findall(r"\d+", file.readline()):
    accumulator += partial_value
  race[i] = int(accumulator)

for time_holding in range(1, race[0]):
  if ((race[0]- time_holding) * time_holding > race[1]):
    result += 1

print("Las formas de ganar la carrera son: " + str(result))
file.close()
