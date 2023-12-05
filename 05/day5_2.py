#!/usr/bin/python3

# Dia 5 parte 2
# See:  https://adventofcode.com/2023/day/5
# Date: 05/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = "data"
      
try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

current_seed_values = []
for start, length in re.findall(r"(\d+) (\d+)", file.readline()):
  current_seed_values.append(range(int(start), int(start)+int(length)))

next_seed_values = []
for line in file:
  data = re.findall(r"(\d+)",line)
  
  if (not data): 
    if (next_seed_values != []): # Cambio de sección
      print("Siguiente seccion\n")
      current_seed_values = current_seed_values + next_seed_values
      next_seed_values = []
    continue

  input_value = int(data[1])
  input_range = range(input_value, input_value+int(data[2]))
  output_change = int(data[0]) - input_value
  
  current_seed_values_copy = current_seed_values.copy()
  for current_range in current_seed_values_copy:
    # Ojo, al último elemento del rango se le debe sumar 1 ([-1] = end - 1)
    intersection = range(max(current_range[0], input_range[0]), min(current_range[-1], input_range[-1]) + 1)

    print("Current range: ", current_range, "Catching range:", input_range, "dif: ", output_change)
    if (len(intersection) > 0):
      print("Añadido", range(intersection[0] + output_change, intersection[-1] + 1 + output_change))
      # Ojo, al último elemento del rango se le debe sumar 1 ([-1] = end - 1)
      next_seed_values.append(range(intersection[0] + output_change, intersection[-1] + 1 + output_change))
      
      remainder_before = range(current_range[0], input_range[0]-1)
      if (len(remainder_before) > 0):
        print("Añadido antes: ", remainder_before)
        current_seed_values.append(remainder_before)

      remainder_after = range(input_range[-1]+2, current_range[-1]+1)
      if (len(remainder_after) > 0):
        print("Añadido dps: ", remainder_after)
        current_seed_values.append(remainder_after)
      current_seed_values.remove(current_range)
    print("valores: ", current_seed_values)

current_seed_values = current_seed_values + next_seed_values
min_value = current_seed_values[0][0] # First seed of the first range
for seed_range in current_seed_values:
  if(seed_range[0] < min_value):
    min_value = seed_range[0]

print("El menor resultado es:", min_value)
file.close()
