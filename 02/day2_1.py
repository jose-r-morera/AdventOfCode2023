#!/usr/bin/python3

# Dia 2 parte 1
# See:  https://adventofcode.com/2023/day/2
# Date: 02/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Dado por el enunciado
cubes_limit = {"red": 12, "green": 13, "blue": 14}
ids_sum = 0

for line in file:
  valid = True

  for cube in cubes_limit:
    string_values = re.findall(r"(\d+) " + cube, line)
    int_values = [int(value) for value in string_values]
 
    if(max(int_values) > cubes_limit[cube]):
      valid = False
      break

  if(valid):
    game_id = int(re.search(r"Game \d+", line)[0][5:])
    ids_sum += game_id

print("La suma de ids es: " + str(ids_sum))
file.close()
