# Imports math library
import math

print("Finding the circumference (C) and the area (A) of a circle using the diameter and pi (3.14)")

# Stores the number that the user enters in the variable 'diameter'
diameter = input("Insert and enter a positive number or decimal to be the diameter of a circle: ")

# Makes a variable 'pi' by defining it as math.pi. Then it turns the variable 'diameter' and 'pi' into decimal numbers
pi = math.pi
diameter = float(diameter)
pi = float(pi)

# Use the print function to show the equation on the console and does the calculations for the area and circumference
print("A = πr^2 =", (diameter / 2) ** 2 * pi, "units^2")
print("C = πd =", diameter * pi, "units")
