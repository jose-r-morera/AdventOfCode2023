#!/usr/bin/python3

# Dia 8 parte 1
# See:  https://adventofcode.com/2023/day/8
# Date: 08/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

instructions_codified = file.readline().replace("R", "1").replace("L", "0")[:-1]
nodes = {}

for line in file:
  data = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)
  if data: nodes[data[0][0]] = data[0][1:]

current_node = "AAA"
steps = 0
while (current_node != "ZZZ"):
  current_node = nodes[current_node][int(instructions_codified[steps%len(instructions_codified)])]
  steps += 1

print("La suma de pasos es: " + str(steps))
file.close()
