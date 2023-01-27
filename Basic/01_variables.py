# Variables 

from audioop import add
from unicodedata import name


my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema

print(len(my_string_variable))

# Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!

name, surname, alias, edad = "Raziel", "Lucio", "Ziel", "31"

print("Me llamo:", name, surname, "Mi edad es:",edad, "y mi alias es:", alias)

# Inputs
"""first_name = input("¿Cual es tu nombre: ")
age = input ("¿Cuantos años tienes?:")
print(first_name)
print(age)
"""

#Cambiamos el tipo
first_name = 31
age = "Raziel"
print(first_name)
print(age)

# ¿Forzamos el tipo?
address: str = "MI dirección"
address: int = 32

print(type(address))