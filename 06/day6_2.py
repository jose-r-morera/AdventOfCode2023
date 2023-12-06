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
race_time = ""
race_distance = ""

total_time = ""
for time in re.findall(r"\d+", file.readline()):
  total_time += time
race_time = int(total_time)

total_distance = ""
for distance in re.findall(r"\d+", file.readline()):
  total_distance += distance
race_distance = int(total_distance)

for time_holding in range(1, race_time):
  if ((race_time - time_holding) * time_holding > race_distance):
    result += 1

print("Las formas de ganar la carrera son: " + str(result))
file.close()

