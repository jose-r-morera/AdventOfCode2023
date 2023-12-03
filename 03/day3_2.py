#!/usr/bin/python3

# Dia 3 parte 2
# See:  https://adventofcode.com/2023/day/3
# Date: 03/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Leer todas las líneas del fichero
lines = file.readlines()

gears_sum = 0
line_numbers = {}
for i in range(len(lines)):
  line_numbers[i] = []

# Almacenamos los números de la primera línea
for digit in re.finditer(r"\d+", lines[0]):
      line_numbers[0].append(tuple([digit.start(), int(digit.group())]))

for line_index in range(len(lines)):
  # Almacenamos los números de la siguiente línea
  if(line_index + 1 < len(lines)):
    for digit in re.finditer(r"\d+", lines[line_index+1]):
      line_numbers[line_index+1].append(tuple([digit.start(), int(digit.group())]))

  for char_index in range(len(lines[line_index])-1):
    char = lines[line_index][char_index]
    if(char == "*"):
      # Hay un posible "engranaje", miramos adyacencia
      adjacent_count = 0
      current_gear_sum = 1
      for i in [-1, 0, 1]:
        # Obtenemos los números de la línea
        numbers = line_numbers[line_index+i] 
        for j in [-1, 0, 1]:
          if(i == 0 and j == 0):
            continue
          for number in numbers:
            if(number[0] <= char_index+j and number[0]+(len(str(number[1]))-1) >= char_index+j):
              numbers.remove(number)
              adjacent_count += 1
              current_gear_sum *= number[1]
      if(adjacent_count == 2):
        gears_sum += current_gear_sum

print("La suma de partes es: " + str(gears_sum))
file.close()
