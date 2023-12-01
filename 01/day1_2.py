#!/usr/bin/python3

# Dia 1 parte 1
# See:  https://adventofcode.com/2023/day/1
# Date: 01/12/2023
__author__ = "José Ramón Morera Campos"

import re # regex

nombre_archivo = input("Introduzca la ruta del archivo: ")

try:
  archivo = open(nombre_archivo, "r")
except:
  print("No se pudo abrir el fichero", nombre_archivo)
  exit()

# Sustituimos un número por su valor numérico además de mantener su primera y última letra para mantener los números superpuestos
numbers_replacement = {"one" :"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"9e"}

suma = 0
for linea in archivo:
  for number in numbers_replacement:
    linea = linea.replace(number, numbers_replacement[number])

  digits = re.findall(r'\d', linea)
  print(digits)
  suma += int(digits[0]+digits[-1])


print("La suma es: " + str(suma))
archivo.close()
