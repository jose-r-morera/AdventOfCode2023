import sys
import re # regex

nombre_archivo = input("Introduzca la ruta del archivo: ")

try:
  archivo = open(nombre_archivo, "r")
except:
  print("No se pudo abrir el fichero", nombre_archivo)
  exit()

numbers_value = {"one" :"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"9e"}

suma = 0
for linea in archivo:
  for number in numbers_value:
    linea = linea.replace(number, numbers_value[number])

  digits = re.findall(r'\d', linea)
  print(digits)
  suma += int(digits[0]+digits[-1])


print("La suma es: " + str(suma))
archivo.close()
