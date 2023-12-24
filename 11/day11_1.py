#!/usr/bin/python3

# Dia 11 parte 1
# See:  https://adventofcode.com/2023/day/11
# Date: 24/12/2023
__author__ = "José Ramón Morera Campos"

import numpy as np # matrix
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

map = np.array([x for x in file.readline()[:-1]])
for line in file:               # Construimos el mapa fila a fila
  line_list = [x for x in line[:-1]]
  map = np.vstack((map, line_list))
  if line_list.count('.') == len(line_list): # Expandimos filas sin galaxias
    map = np.vstack((map, line_list))

inserted_count = 0
for index, col in enumerate(map.T):
  if col.tolist().count('.') == len(col): # Expandimos filas sin galaxias
    map = np.hstack((map[:,:index+ inserted_count], col[:, np.newaxis], map[:,index+inserted_count:]))
    inserted_count += 1

# Encontramos galaxias
galaxies = []
for row_index,row in enumerate(map):
  for col_index, col in enumerate(row):
    if(col == '#'):
      galaxies.append((row_index, col_index))

distance_sum = 0 # Total
for count, galaxy in enumerate(galaxies[:-1]):
  for aux_galaxy in galaxies[(count+1):]:
    distance_sum += (abs(galaxy[0]-aux_galaxy[0]) + abs(galaxy[1]-aux_galaxy[1]))
    #print(count+1, galaxy, aux_galaxy, distance_sum, (abs(galaxy[0]-aux_galaxy[0]) + abs(galaxy[1]-aux_galaxy[1])))


print("La suma de puntos es: " + str(distance_sum))
file.close()
