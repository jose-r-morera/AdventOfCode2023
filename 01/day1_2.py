#!/usr/bin/python3

# Dia 1 parte 2
# See:  https://adventofcode.com/2023/day/1
# Date: 01/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

file_name = input("Introduzca la ruta del archivo: ")

try:
  file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

# Sustituimos un número por su valor numérico además de mantener su primera y última letra para mantener los números superpuestos
numbers_replacement = {"one" :"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"9e"}

sum = 0
for line in file:
  for number in numbers_replacement:
    line = line.replace(number, numbers_replacement[number])

  digits = re.findall(r'\d', line)
  print(digits)
  sum += int(digits[0]+digits[-1])


print("La suma es: " + str(sum))
file.close()
