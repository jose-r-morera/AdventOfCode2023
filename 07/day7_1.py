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
  cards[value] = [bid, 0]

for card_value in cards:
  value_count = {"A":0, "K":0, "Q":0, "J":0, "T":0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}
  for digit in card_value:
    value_count[digit] += 1
  most_repeated_card_cound = max(value_count.values())
  value_count.pop(max(value_count, key=value_count.get))
  second_repeated_card_count = max(value_count.values())

  # Se podria hacer con un array y un enumerate
  if(most_repeated_card_cound == 5): 
    cards[card_value][1] = 60000000000
  elif (most_repeated_card_cound == 4):
    cards[card_value][1] = 50000000000
  elif (most_repeated_card_cound == 3 and second_repeated_card_count == 2): # Full house
    cards[card_value][1] = 40000000000
  elif (most_repeated_card_cound == 3 and second_repeated_card_count == 1): 
    cards[card_value][1] = 30000000000
  elif (most_repeated_card_cound == 2 and second_repeated_card_count == 2): 
    cards[card_value][1] = 20000000000
  elif (most_repeated_card_cound == 2): 
    cards[card_value][1] = 10000000000
  else:
    cards[card_value][1] = 0

face_points = {"A":13, "K":12, "Q":11, "J":10, "T":9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
for card_value in cards:
  pow = 1
  for digit in range(0,5):
    cards[card_value][1] += face_points[card_value[4-digit]] * pow
    pow *= 100

rank = 1
total_winnings = 0
for card in sorted(cards.items(), key=lambda item: item[1][1]):
  total_winnings += int(card[1][0]) * rank
  rank += 1

print("La suma de puntos es: " + str(total_winnings))
file.close()
