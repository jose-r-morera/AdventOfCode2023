#!/usr/bin/python3

# Dia 7 parte 1
# See:  https://adventofcode.com/2023/day/7
# Date: 07/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex
import sys

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

cards = {}
for card in file:
  value, bid = re.findall(r"(.*) (.*)", card)[0]
  cards[value] = bid

ordered_cards = []
#ordenar jejej

points_sum = 0 # Total
print(cards)



print("La suma de puntos es: " + str(points_sum))
file.close()
