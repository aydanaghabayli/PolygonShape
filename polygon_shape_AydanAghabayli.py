
#The program calculates polygons areas for entered polygon points and a sum of all circle areas
#Created by Aydan Aghabayli

import math

print("The Python program calculates polygons areas for entered polygon points and a sum of all circle areas")
print()


# Input number of points. Defined condition.
while 1:
    n = int(input("Enter number of polygon points: "))  
    if n>=3:
        break
    else:
        print("Define at least three points to create a polygon!")



# A list that stores all entered polygon points. It is empty at start.
points_x = []
points_y = []

# Input all points
print("Enter point coordinates ...")
for i in range(n):
    x = float(input(f"x[{i+1}]: "))
    y = float(input(f"y[{i+1}]: "))
    points_x.append(x)
    points_y.append(y)

#Table for showing polygon coordinates (x,y)
print("Polygon coordinates table")
print()
print(f"{'i':>5} {'X':>10} {'Y':>10}")
print("-" * 43)
for i in range(n):
    print(f"{i + 1:5} {points_x[i]:10.2f} {points_y[i]:10.2f}")

#Definition to able to sum
Ax = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0

#Formulas for properties
for i in range(n-1):
    Ax = Ax + ((points_x[i+1] + points_x[i])*(points_y[i+1] - points_y[i]))/2
    Sx = Sx + (points_x[i+1] - points_x[i]) * (points_y[i+1]**2 + points_y[i] * points_y[i+1] + points_y[i]**2)
    Sy = Sy + (points_y[i+1] - points_y[i]) * (points_x[i+1]**2 + points_x[i] * points_x[i+1] + points_x[i]**2)
    Ix = Ix + (points_x[i+1] - points_x[i]) * (points_y[i+1]**3 +  points_y[i+1]**2 * points_y[i] + points_y[i+1] * points_y[i]**2 + points_y[i]**3)
    Iy = Iy + (points_y[i+1] - points_y[i]) * (points_x[i+1]**3 +  points_x[i+1]**2 * points_x[i] + points_x[i+1] * points_x[i]**2 + points_x[i]**3)
    Ixy = Ixy + (points_y[i+1] - points_y[i]) * (points_y[i+1] * (3* points_x[i+1]**2 + 2 * points_x[i] * points_x[i+1] + points_x[i]**2) + points_y[i] * (3 * points_x[i]**2 + 2 * points_x[i] * points_x[i+1] + points_x[i+1]**2))

#Final calculations
Ax = 0.5*Ax
Sx = -Sx/6
Sy = Sy/6
Ix = -Ix/12
Iy = Iy/12
Ixy = -Ixy/24
xt = Sy/Ax
yt = Sx/Ax
Ixt = Ix - (yt**2*Ax)
Iyt = Iy - (xt**2*Ax)
Ixyt = Ixy + xt*yt*Ax


# Print a table of entered data and calculated values
print()
print("Geometric properties:")
print("\n")

print (f'{"Ax:"} {Ax:10.2f}')
print (f'{"Sx:"} {Sx:10.2f}')
print (f'{"Sy:"} {Sy:10.2f}')
print (f'{"Ix:"} {Ix:10.2f}')
print (f'{"Iy:"} {Iy:10.2f}')
print (f'{"Ixy:"} {Ixy:10.2f}')
print (f'{"xt:"} {xt:10.2f}')
print (f'{"yt:"} {yt:10.2f}')
print (f'{"Ixt:"} {Ixt:10.2f}')
print (f'{"Iyt:"} {Iyt:10.2f}')
print (f'{"Ixyt:"} {Ixyt:10.2f}')

print()
print("End.")


