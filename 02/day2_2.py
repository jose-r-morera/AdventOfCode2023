#!/usr/bin/python3

# Dia 2 parte 2
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

cubes = ["red", "green", "blue"]
cubes_power_sum = 0

for line in file:
  current_power = 1

  for cube in cubes:
    string_values = re.findall(r"(\d+) " + cube, line)
    int_values = [int(value) for value in string_values]
 
    current_power *= max(int_values)
  
  cubes_power_sum += current_power

print("La suma de potencias de cubos es: " + str(cubes_power_sum))
file.close()
