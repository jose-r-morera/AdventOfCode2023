#!/usr/bin/python3

# Dia 9 parte 1
# See:  https://adventofcode.com/2023/day/9
# Date: 09/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

next_value_sum = 0 # Total

for line in file:
  numbers = [[int(x) for x in line.split()]]
  current_line = 0
  while(len(numbers[current_line]) > 1 and not all (n == 0 for n in numbers)):  # Calculamos la diferencia hasta que quede un elemento o todos sean 0
    numbers.append([])
    for i in range(0,len(numbers[current_line])-1):
      numbers[current_line + 1].append(numbers[current_line][i+1] - numbers[current_line][i])
    current_line += 1

  while(current_line > 0): # Extrapolamos el siguiente valor
    current_line -= 1
    numbers[current_line].append(numbers[current_line][-1] + numbers[current_line + 1][-1])
  next_value_sum += numbers[0][-1]

print("La suma de puntos es: " + str(next_value_sum))
file.close()
