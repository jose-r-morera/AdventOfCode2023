#!/usr/bin/python3

# Dia 5 parte 1
# See:  https://adventofcode.com/2023/day/5
# Date: 05/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

#file_name = input("Introduzca la ruta del archivo: ")
file_name = "data"

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

seeds = []
for seed in re.findall(r"(\d+)", file.readline()):
  seeds.append([int(seed), int(seed), False])

for line in file:
  data = re.findall(r"(\d+)",line)
  if (data == []):
    for i, _ in enumerate(seeds):
      seeds[i][2] = False
    continue
  src = int(data[1])
  src_range = range(src, src+int(data[2]))
  dst = int(data[0])

  for i, _ in enumerate(seeds):
    if(seeds[i][2] == False and seeds[i][1] in src_range):
      #print("La semilla ", seeds[i][0], "corresponde", (seeds[i][1]-src+dst))
      seeds[i][1] = seeds[i][1] - src + dst
      seeds[i][2] = True

min = seeds[1][1]
for seed in seeds:
  if(seed[1] < min):
    min = seed[1]

print("La suma de puntos es: ", min)
file.close()
