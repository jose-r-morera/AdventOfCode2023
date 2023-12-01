import sys
import re # regex

nombre_archivo = input("Introduzca la ruta del archivo: ")

try:
  archivo = open(nombre_archivo, "r")
except:
  print("No se pudo abrir el fichero", nombre_archivo)

numbers = {"one" :1, "two":2, "trhee":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

suma = 0
for linea in archivo:
  first = {"one" :-1, "two":-1, "three":-1, "four":-1, "five":-1, "six":-1, "seven":-1, "eight":-1, "nine":-1}
  last = {"one" :-1, "two":-1, "three":-1, "four":-1, "five":-1, "six":-1, "seven":-1, "eight":-1, "nine":-1}
  for number in first:
    if(linea.find(number) > -1):
      first[number] = linea.find(number)
    if(linea.rfind(number) > -1):
      last[number] = linea.find(number)
  first_number = min(first, key=first.get)
  last_number = max(last, key=last.get)
  print(first_number)

  if(first_number != -1):
    line_with_nubmers = linea.replace(first_number, str(numbers[first_number]))
  if(last_number != -1):
    line_with_nubmers = line_with_nubmers.replace(last_number, str(numbers[last_number]))

  digits = re.findall(r'\d', line_with_nubmers)
  print(digits)
  suma += int(digits[0]+digits[-1])


print("La suma es: " + str(suma))
archivo.close()