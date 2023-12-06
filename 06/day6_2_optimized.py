#!/usr/bin/python3

# Dia 6 parte 2
# See:  https://adventofcode.com/2023/day/6
# Date: 06/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys
import math

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

race = [0,0] # Carrera formada por [tiempo, distancia]

for i in [0, 1]:
  accumulator = ""
  for partial_value in re.findall(r"\d+", file.readline()):
    accumulator += partial_value
  race[i] = int(accumulator) + i # Debemos superar la distancia

time = race[0]
distance = race[1]
winning_combinations = math.floor((time+math.sqrt(time*time-4*distance))/2) - math.ceil((time-math.sqrt(time*time-4*distance))/2) + 1

print("Las formas de ganar la carrera son: " + str(winning_combinations))
file.close()
