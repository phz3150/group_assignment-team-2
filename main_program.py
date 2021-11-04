#!/usr/bin/env python

import numpy as np


#create array of x coordinates:

x = -10. + np.arange(0, 20.1, 0.1) 

# ask for input R:
R = float(input('R = '))
def volume(R):
  """Calculates the volume of a sphere with a given radius."""
  import numpy as np
  V = (4 / 3) * np.pi * (R ** 3)
  return V
# call the external functions:
y = coordinates(x,R)
D_SA = sphere_properties(R)
V = volume(R)
# print informative statements:
print( 'A sphere of radius %.2f has a diameter of %.2f , a surface area of %.2f , and a volume of %.2f .' %(R, D_SA[0], D_SA[1], V))
print( 'The y-coordinates of a circle with radius', R, ' are \n', y)
