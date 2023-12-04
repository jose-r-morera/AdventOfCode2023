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

cards = []  # Almacena pares (contenido, número de tarjetas ganadas de ese tipo)
for line in file:
  cards.append([line, 1])

cards_sum = 0 # Valor a calcular: número de tarjetas ganadas

index = 0
for card, count in cards:
  cards_sum += count
  
  first_part = re.search(r"\: .+ \|", card).group(0)
  winning_string_values = re.findall(r"\d+", first_part)
  winning_int_values = [int(value) for value in winning_string_values]

  second_part = re.search(r'\| .+', card).group(0)
  numbers_string_values = re.findall(r"\d+", second_part)
  numbers_int_values = [int(value) for value in numbers_string_values]
  
  current_points = 0
  for number in numbers_int_values:
    if(number in winning_int_values):
      current_points += 1
      if(index + current_points < len(cards)):
        cards[index + current_points][1] += count
  index += 1

print("El número de tarjetas obtenidas es: " + str(cards_sum))
file.close()
