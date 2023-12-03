#!/usr/bin/python3

# Dia 3 parte 1
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

parts_sum = 0 # Resultado final
lines = file.readlines() # Todas las líneas del fichero

# Diccionario en el que para cada línea almacenamos pares [posición, número]
line_numbers = {}
for i in range(len(lines)):
  line_numbers[i] = []

# Almacenamos los números de la primera línea
for number in re.finditer(r"\d+", lines[0]):
  line_numbers[0].append(tuple([number.start(), int(number.group())]))

for line_index in range(len(lines)):
  # Almacenamos los números de la siguiente línea
  if(line_index + 1 < len(lines)):
    for number in re.finditer(r"\d+", lines[line_index+1]):
      line_numbers[line_index+1].append(tuple([number.start(), int(number.group())]))

  for char_index in range(len(lines[line_index])-1):
    char = lines[line_index][char_index]
    if(char != "." and not char.isnumeric()):
      # Hay caracter especial, miramos adyacencia
      for i in [-1, 0, 1]:
        numbers = line_numbers[line_index+i] # Números que hay en la línea
        for j in [-1, 0, 1]:
          if(i == 0 and j == 0):
            continue
          for number in numbers:  # Para cada número de la línea vemos si es adyacente
            if(number[0] <= char_index+j and number[0]+(len(str(number[1]))-1) >= char_index+j):
              parts_sum += number[1] 
              numbers.remove(number)
      
print("La suma de partes es: " + str(parts_sum))
file.close()
