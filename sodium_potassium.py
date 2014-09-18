from visual import *

count = 0
for i in range(6):
  for j in range(6):
    for k in range(6):
      count = i + j + k
      molecule1 = sphere(radius = 0.3, pos=[i,j,k], color=color.red)
      if count%2 == 0:
        molecule2 = sphere(radius = 0.3, pos=[i,j,k], color=color.blue)
