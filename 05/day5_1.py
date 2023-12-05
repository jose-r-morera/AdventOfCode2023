#!/usr/bin/python3

# Dia 5 parte 1
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

seeds = [] # Pares [valor, procesado] (procesado indica si ya se ha cambiado en la sección actual)
for seed in re.findall(r"(\d+)", file.readline()):
  seeds.append([int(seed), False])

for line in file:
  data = re.findall(r"(\d+)",line)
  if (not data):
    for i, _ in enumerate(seeds):
      seeds[i][1] = False
    continue
  src = int(data[1])
  src_range = range(src, src+int(data[2]))
  dst = int(data[0])

  for i, _ in enumerate(seeds):
    if(seeds[i][1] == False and seeds[i][0] in src_range):
      seeds[i][0] = seeds[i][0] - src + dst
      seeds[i][1] = True

min = seeds[1][0]
for seed in seeds:
  if(seed[0] < min):
    min = seed[0]

print("El menor valor obtenido es: ", min)
file.close()
