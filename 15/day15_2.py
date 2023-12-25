#!/usr/bin/python3

# Dia 15 parte 2
# See:  https://adventofcode.com/2023/day/15
# Date: 25/12/2023
__author__ = "José Ramón Morera Campos"

import sys
import re # regex

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

def hash_algorithm(string):
  current_value = 0
  for char in string:
    current_value += ord(char)
    current_value *= 17
    current_value %= 256
  return current_value

boxes = [[] for _ in range(0, 256)] # Cada caja es un array [tag, focus]

instructions = file.readline().split(',')
for step in instructions:
  tag, info = re.findall(r'(.*)(=.*|-)', step)[0]
  box_id = hash_algorithm(tag)

  if step[-1] == '-':
    for index, lens in enumerate(boxes[box_id]):
      if lens[0] == tag:
        boxes[box_id].pop(index)
  else:
    exists = False
    for index, lens in enumerate(boxes[box_id]):
      if lens[0] == tag:                          # Actualizamos
        boxes[box_id][index] = [tag, int(info[1:])]
        exists = True
        break
    if not exists:
      boxes[box_id].append([tag, int(info[1:])])

total_sum = 0 # Total
for box_index, box in enumerate(boxes):
  for lens_index, lens in enumerate(box):
    total_sum += (box_index+1)*(lens_index+1)*lens[1]
    
print("La suma de puntos es: " + str(total_sum))
file.close()
