#!/usr/bin/python3

# Dia 7 parte 2
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

cards = {}  # Representamos cada carta como una dupla [bid, valor_numérico]
for line in file:
  value, bid = re.findall(r"(.*) (.*)", line)[0]
  cards[value] = [bid, 0]

face_points = {"A":13, "K":12, "Q":11, "J":0, "T":9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
for card_value in cards:
  joker = 0 # Contamos los joker como comodín
  value_count = {"A":0, "K":0, "Q":0, "T":0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}
  for digit in card_value:
    if digit == "J": joker += 1
    else:   value_count[digit] += 1 # Establecemos cuántas cartas de cada tipo tiene la mano
  most_repeated_card_cound = max(value_count.values()) + joker  # Cantidad máxima de repeticiones, incluimos los joker
  value_count.pop(max(value_count, key=value_count.get))
  second_repeated_card_count = max(value_count.values()) # Segundo máximo de repeticiones

  for i, values in enumerate([[5, 0], [4, 1], [3, 2], [3, 1], [2, 2], [2, 1], [1, 1]]): # Combinaciones de las manos, en orden decreciente
    if([most_repeated_card_cound, second_repeated_card_count] == values): 
      cards[card_value][1] = (6-i)*10000000000  # Asignamos valor según el tipo de mano
      break
  
  pow = 1
  for digit in range(0,5):  # Asignamos valor según cada dígito
    cards[card_value][1] += face_points[card_value[4-digit]] * pow
    pow *= 100

total_winnings = 0
for index, card in enumerate(sorted(cards.items(), key=lambda item: item[1][1])):
  total_winnings += int(card[1][0]) * (index + 1)

print("La suma de puntos es: " + str(total_winnings))
file.close()
