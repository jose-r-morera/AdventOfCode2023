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
  races.append([time, 0])

count = 0
for distance in re.findall(r"\d+", file.readline()):
  races[count][1] = distance
  count += 1

for race in races:
  time = int(race[0])
  distance = int(race[1])
  race_count = 0

  for time_holding in range(1, time):
    if ((time - time_holding) * time_holding > distance):
      print(time_holding)
      race_count += 1
  print("cuenta:", race_count)
  result *= race_count

print(races)

print("La suma de puntos es: " + str(result))
file.close()
