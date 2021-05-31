from sense_hat import SenseHat
import time, random
import numpy as test

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def setCherry(map):
  randNum = random.randint(0,56)
  if map[randNum] == 0:
    map[randNum] = 3
  else:
    return setCherry(map)
  return map

def setGrape(map):
  randNum = random.randint(0,56)
  if map[randNum] == 0:
    map[randNum] = 2
  else:
    return setGrape(map)
  return map

map = [0] * 56
map[0] = 1
mapWithCherries = [] * 56
for x in range(5):
  mapWithCherries = setCherry(map)
mapWithGrape = setGrape(mapWithCherries)

def makeColorMap(map):
  newMap = [nothing] * 56
  for x in range(56):
    if map[x] == 1: 
      newMap[x] = white
    elif map[x] == 2: 
      newMap[x] = green
    elif map[x] == 3: 
      newMap[x] = red
  return newMap

colorMap = makeColorMap(mapWithGrape) + [nothing] * 8
s.set_pixels(colorMap)
