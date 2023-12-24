#!/usr/bin/python3

# Dia 11 parte 2
# See:  https://adventofcode.com/2023/day/11
# Date: 24/12/2023
__author__ = "José Ramón Morera Campos"

import sys
import numpy as np

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

astro_map = np.array([x for x in file.readline()[:-1]])
for line in file:                                        # Construimos el mapa fila a fila
  line_list = [x for x in line[:-1]]
  astro_map = np.vstack((astro_map, line_list))

# Almacenamos galaxias fila a fila
galaxies = []
empty_rows = []
for row_index,row in enumerate(astro_map):  
  if row.tolist().count('.') == len(row): # Fila sin galaxias
    empty_rows.append(row_index)
  else: 
    for col_index, col in enumerate(row):
      if(col == '#'):
        galaxies.append([row_index, col_index])

empty_cols = [] 
for col_index, col in enumerate(astro_map.T):
  if col.tolist().count('.') == len(col): # Expandimos filas sin galaxias
    empty_cols.append(col_index)

GAP = 999999 # 1 +999999 = 1000000
empty_row_count = 0
for gal_index, galaxy in enumerate(galaxies):
  if empty_row_count < len(empty_rows) and galaxy[0] > empty_rows[empty_row_count]:
    empty_row_count += 1

  empty_col_count = sum(1 for col in empty_cols if galaxy[1] > col)
  
  galaxies[gal_index] = [galaxy[0] + GAP * empty_row_count, galaxy[1] + GAP * empty_col_count]

print(galaxies)
distance_sum = 0 # Total
for count, galaxy in enumerate(galaxies[:-1]):
  for aux_galaxy in galaxies[(count+1):]:
    distance_sum += (abs(galaxy[0]-aux_galaxy[0]) + abs(galaxy[1]-aux_galaxy[1]))

print("La suma de puntos es: " + str(distance_sum))
file.close()
