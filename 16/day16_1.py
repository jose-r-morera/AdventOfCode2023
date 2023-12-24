#!/usr/bin/python3

# Dia 16 parte 1
# See:  https://adventofcode.com/2023/day/16
# Date: 24/12/2023
__author__ = "José Ramón Morera Campos"

import sys
from collections import deque # Cola eficiente

if (len(sys.argv) > 1): file_name = sys.argv[1]
else: file_name = input("Introduzca la ruta del archivo: ")

try: file = open(file_name, "r")
except:
  print("No se pudo abrir el fichero", file_name)
  exit()

maze = []
for line in file:
  row = []
  for column in line[:-1]:   
    row.append([column,  [0,0,0,0]]) # Array N, S, E, W
  maze.append(row)

CARDINALS = {'N':0, 'S':1, 'E':2, 'W':3}
def in_maze(coords):
  if coords[0] < len(maze) and coords[0] >= 0 and  coords[1] >= 0 and coords[1] < len(maze[0]):
    return True
  else:
    return False

def not_visited(pos, mov):
  visited = maze[pos[0]][pos[1]][1]
  if visited[CARDINALS[mov]]: return False
  else: return True

movement = {'N':(-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}
beams = deque([[(0,0), 'E']])  # Usado como una cola
while beams:
  beam_pos, beam_mov = beams[0]
  while in_maze(beam_pos) and not_visited(beam_pos, beam_mov):
    current_element = maze[beam_pos[0]][beam_pos[1]][0]
    maze[beam_pos[0]][beam_pos[1]][1][CARDINALS[beam_mov]] = 1 # Marcamos la casilla como visitada por una flecha de este tipo
    match current_element:
      case '|':
        if beam_mov == 'E' or beam_mov == 'W': # Split
          beam_mov = 'S'
          beams.append([beam_pos, 'N'])
      case '\\':
        if beam_mov == 'N': beam_mov = 'W'
        elif beam_mov == 'W': beam_mov = 'N'
        elif beam_mov == 'S': beam_mov = 'E'
        else: beam_mov = 'S'
      case '-':
        if beam_mov == 'N' or beam_mov == 'S': # Split
          beam_mov = 'W'
          beams.append([beam_pos, 'E'])
      case '/':
        if beam_mov == 'N': beam_mov = 'E'
        elif beam_mov == 'E': beam_mov = 'N'
        elif beam_mov == 'S': beam_mov = 'W'
        else: beam_mov = 'S'
    beam_pos = (beam_pos[0] + movement[beam_mov][0], beam_pos[1] + movement[beam_mov][1]) # Actualizamos posicion
  beams.popleft()

energyzed_beams = 0
for row in maze:
  for col in row:
    if col[1] != [0, 0, 0, 0]:
      print('#', end='')
      energyzed_beams += 1
    else:
      print(col[0], end='')
  print()

print("La suma de puntos es: " + str(energyzed_beams))
file.close()
