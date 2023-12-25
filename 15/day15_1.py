#!/usr/bin/python3

# Dia 15 parte 1
# See:  https://adventofcode.com/2023/day/15
# Date: 25/12/2023
__author__ = "José Ramón Morera Campos"

import sys

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

total_sum = 0 # Total
instructions = file.readline().split(',')
for step in instructions:
  print(step, hash_algorithm(step))
  total_sum += hash_algorithm(step)

print("La suma de puntos es: " + str(total_sum))
file.close()
