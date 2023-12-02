#!/usr/bin/python3

# Dia 2 parte 1
# See:  https://adventofcode.com/2023/day/2
# Date: 02/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

nombre_archivo = input("Introduzca la ruta del archivo: ")

try:
  archivo = open(nombre_archivo, "r")
except:
  print("No se pudo abrir el fichero", nombre_archivo)
  exit()

# Dado por el enunciado
cubes_limit = {"red": 12, "green": 13, "blue": 14}
ids_sum = 0

for linea in archivo:
  valid = True
  max_cubes = {"red": 0, "green": 0, "blue": 0}
  for cube in cubes_limit:
    string_values = re.findall(r"(\d+) " + cube, linea)
    int_values = [int(value) for value in string_values]
    max_cubes[cube] = max(int_values)
    if(max_cubes[cube] > cubes_limit[cube]):
      valid = False
      break
    
  if(valid):
    game_id = int(re.search(r"Game \d+", linea)[0][5:])
    ids_sum += game_id

print("La suma de ids es: " + str(ids_sum))
archivo.close()
