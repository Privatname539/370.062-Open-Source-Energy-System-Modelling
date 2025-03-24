# This program will calculate the area of a circle and volume of a sphere for a given radius

import numpy as np                  # Pi will be imported from numpy, alternatively the math module can be imported for Pi

r = int(input("Enter radius: "))    # Enter radius of circle or sphere

A = np.pi*(r**2)                    # Calculates area of circle for given radius

V = (4/3)*(r**3)*np.pi              # Calculates volume of sphere for given radius

print("Radius: ", r)                # Outputs the given radius
print("Area: ", round(A,2))         # Outputs the result for area rounded to 2 decimal places
print("Volume: ", round(V,2))       # Outputs the result for volume rounded to 2 decimal places