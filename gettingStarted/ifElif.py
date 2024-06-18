#This code was originally written in Python 2.7 (?) during the course I realized that the Python package installed on my PC was incorrect. Adapted for the assignment and then installed Python 3 to work with in the remaining projects.

# coding=utf-8
print("Your color choices are red, blue, green, white or yellow")
userColor = raw_input("Enter color: ").lower()

if userColor == "red":
    print("Red in Spanish is \"Rojo\".")
elif userColor == "blue":
    print("Blue in Spanish is \"Azul\".")
elif userColor == "green":
    print("Green in Spanish is \"Verde\".")
elif userColor == "white":
    print("White in Spanish is \"Blanco\".")
elif userColor == "yellow":
    print("Yellow in Spanish is \"Amarillo\".")
else:
    print("That is not a valid color for this program. Ese no es un color válido")

"""
somehow my version is an older version of python and I had to use raw_input rather than input for the code to work correctly.
"""
