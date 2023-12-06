#!/usr/bin/python3

# Dia 6 parte 1
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

result = 1 # Multiplicacion de las formas de ganar
races = []

for time in re.findall(r"\d+", file.readline()):
  races.append([int(time), 0])

for  index, distance in enumerate(re.findall(r"\d+", file.readline())):
  races[index][1] = int(distance)

for time, distance in races:
  race_win_count = 0

  for time_holding in range(1, time):
    if ((time - time_holding) * time_holding > distance):
      race_win_count += 1
  result *= race_win_count

print("La suma de puntos es: " + str(result))
file.close()
