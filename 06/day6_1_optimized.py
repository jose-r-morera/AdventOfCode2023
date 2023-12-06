#!/usr/bin/python3

# Dia 6 parte 1
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

result = 1 # Multiplicacion de las formas de ganar
races = []

for time in re.findall(r"\d+", file.readline()):
  races.append([int(time), 0])

for  index, distance in enumerate(re.findall(r"\d+", file.readline())):
  races[index][1] = int(distance)

for time, distance in races: # distance = x*y; time = x+y (x = time holding = speed, y = time racing)
  distance += 1 # Debemos superar la distancia
  winning_combinations = math.floor((time+math.sqrt(time*time-4*distance))/2) - math.ceil((time-math.sqrt(time*time-4*distance))/2) + 1

  result *= winning_combinations

print("La suma de puntos es: " + str(result))
file.close()
