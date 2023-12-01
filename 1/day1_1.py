import sys
import re # regex

nombre_archivo = input("Introduzca la ruta del archivo: ")

try:
  archivo = open(nombre_archivo, "r")
except:
  print("No se pudo abrir el fichero", nombre_archivo)

suma = 0
for linea in archivo:
  digits = re.findall(r'\d', linea)
  suma += int(digits[0]+digits[-1])


print("La suma es: " + str(suma))
archivo.close()