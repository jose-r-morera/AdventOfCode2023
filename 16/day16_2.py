#!/usr/bin/python3

# Dia 16 parte 2
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
    row.append(column) 
  maze.append(row)

CARDINALS = {'N':0, 'S':1, 'E':2, 'W':3}

def in_maze(coords):
  if coords[0] < len(maze) and coords[0] >= 0 and  coords[1] >= 0 and coords[1] < len(maze[0]): return True
  else: return False

def not_visited(pos, mov, data):
  visited = data[pos[0]][pos[1]]
  if visited[CARDINALS[mov]]: return False
  else: return True

movement = {'N':(-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}

def solve(start_pos, start_move):
  beams = deque([[start_pos, start_move]])  # Usado como una cola
  visited_data = [[[0, 0, 0, 0] for _ in range(len(maze[0]))] for _ in range(len(maze))]

  while beams:
    beam_pos, beam_mov = beams[0]
    while in_maze(beam_pos) and not_visited(beam_pos, beam_mov, visited_data):
      current_element = maze[beam_pos[0]][beam_pos[1]][0]
      visited_data[beam_pos[0]][beam_pos[1]][CARDINALS[beam_mov]] = 1 # Marcamos la casilla como visitada por una flecha de este tipo
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

  energyzed_tiles = 0
  for row in visited_data:
    for col in row:
      if col != [0, 0, 0, 0]:
        energyzed_tiles += 1
  return energyzed_tiles

tiles_list = []
for row in range(len(maze)):
  tiles_list.append(solve((row,0), 'E'))
  tiles_list.append(solve((row,len(maze[0])), 'W'))
for column in range(len(maze[0])):
  tiles_list.append(solve((0,column), 'S'))
  tiles_list.append(solve((len(maze),column), 'N'))

max_energyzed_tiles = max(tiles_list)

print("La suma de puntos es: " + str(max_energyzed_tiles))
file.close()