#!/usr/bin/python3

# Dia 8 parte 2
# See:  https://adventofcode.com/2023/day/8
# Date: 08/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

# Funcion auxiliar para el mínimo común multiplo
def LCM(a, b): 
    greater = max(a, b) 
    smallest = min(a, b) 
    for i in range(greater, a*b+1, greater): 
        if i % smallest == 0: 
            return i 
######################################################

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

searching_nodes = []
for node in nodes:
  if node[2] == "A": searching_nodes.append(node)

steps = [0]*len(searching_nodes) # Pasos para llegar de cada nodo inicial al final
for index, _ in enumerate(searching_nodes):
  while searching_nodes[index][2] != "Z":
    searching_nodes[index] = nodes[searching_nodes[index]][int(instructions_codified[steps[index]%len(instructions_codified)])]
    steps[index] += 1

lcm = LCM(steps[0], steps[1])  # Como para cada nodo el recorrido hasta el final es cíclico, estarán todos al final
for i in range(2, len(steps)): # cuando se realice el mínimo común múltiplo de los pasos de cada uno
    lcm = LCM(lcm, steps[i])

print("La suma de pasos es: " + str(lcm))
file.close()
