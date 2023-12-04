#!/usr/bin/python3

# Dia 4 parte 2
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

lines = file.readlines() # Todas las líneas del fichero

cards_sum = 0 # Valor a calcular: número de tarjetas ganadas

for line in lines:
  cards_sum += 1
  current_card = int(re.search(r"Card +(\d+):", line).group(1))
  print("Tarjeta actual:", current_card)
  first_part = re.search(r"\: .+ \|", line).group(0)
  winning_string_values = re.findall(r"\d+", first_part)
  winning_int_values = [int(value) for value in winning_string_values]

  second_part = re.search(r'\| .+', line).group(0)
  numbers_string_values = re.findall(r"\d+", second_part)
  numbers_int_values = [int(value) for value in numbers_string_values]
  
  current_points = 0
  for number in numbers_int_values:
    if(number in winning_int_values):
      current_points += 1
      if(current_card + current_points < len(lines)):
        #print("Añadida tarjeta: ", current_card + current_points)
        lines.append(lines[current_card + current_points -1])
  
  current_card += 1

print("El número de tarjetas obtenidas es: " + str(cards_sum))
file.close()
