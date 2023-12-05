#!/usr/bin/python3

# Dia 5 parte 2
# See:  https://adventofcode.com/2023/day/5
# Date: 05/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")
try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

current_seed_values = []  # Valores en cada sección
for start, length in re.findall(r"(\d+) (\d+)", file.readline()):
  current_seed_values.append(range(int(start), int(start)+int(length)))

next_seed_values = [] # Resultados de procesar la actual sección
for line in file:
  data = re.findall(r"(\d+)",line)
  
  if (not data):           # Titulo de seccion o linea vacía
    if (next_seed_values): # Usamos los resultados para saber si hemos cambiado ya de sección
      current_seed_values = current_seed_values + next_seed_values
      next_seed_values = []
    continue

  input_value = int(data[1])
  input_range = range(input_value, input_value + int(data[2]))
  output_change = int(data[0]) - input_value
  
  current_seed_values_copy = current_seed_values.copy() # Usamos una copia para iterar ya que la modificamos
  for current_range in current_seed_values_copy:
    # Ojo, al último elemento del rango se le debe sumar 1 ([-1] = end - 1)
    intersection = range(max(current_range[0], input_range[0]), min(current_range[-1], input_range[-1]) + 1)

    if (len(intersection) > 0):
      # Ojo, al último elemento del rango se le debe sumar 1 ([-1] = end - 1)
      next_seed_values.append(range(intersection[0] + output_change, intersection[-1] + 1 + output_change))
      
      remainder_before = range(current_range[0], input_range[0]-1)
      if (len(remainder_before) > 0):
        current_seed_values.append(remainder_before)

      remainder_after = range(input_range[-1]+2, current_range[-1]+1)
      if (len(remainder_after) > 0):
        current_seed_values.append(remainder_after)
      current_seed_values.remove(current_range) # Eliminamos el valor ya procesado

current_seed_values = current_seed_values + next_seed_values
min_value = current_seed_values[0][0] # Inicializamos con el primer valor del primer rango
for seed_range in current_seed_values:
  if(seed_range[0] < min_value):
    min_value = seed_range[0]

print("El menor resultado es:", min_value)
file.close()
