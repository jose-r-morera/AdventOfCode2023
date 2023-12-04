#!/usr/bin/python3

# Dia 4 parte 1
# See:  https://adventofcode.com/2023/day/4
# Date: 04/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Total
points_sum = 0

for line in file:
  first_part = re.search(r"\: .+ \|", line)
  winning_string_values = re.findall(r"\d+", first_part[0])
  winning_int_values = [int(value) for value in winning_string_values]
  print(winning_int_values)

  second_part = re.search(r'\| .+', line)
  numbers_string_values = re.findall(r"\d+", second_part[0])
  numbers_int_values = [int(value) for value in numbers_string_values]
  
  first = True
  current_points = 0
  for number in numbers_int_values:
    if(number in winning_int_values):
      print(number)
      if first:
        current_points += 1
        first = False
      else:
        current_points *= 2
  points_sum += current_points

print("La suma de puntos es: " + str(points_sum))
file.close()
