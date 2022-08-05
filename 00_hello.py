#  este es un comentario :
#  Nuetro hola mundo en python
print("Hola Mundo")



''' 
Este tambien es un 
comentario 
en varias líneas
'''
#Consultar el tipo de dato
print(type("Hola python"))  # tipo 'str' 
print(type(5))  # tipo 'int' 
print(type(2.5))  # tipo 'float' 
print(type(True))  # tipo 'bool'
print(type(1 + 2j))  # tipo 'Complex'  

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

print(type(print(my_string_variable, str(my_int_variable), my_bool_variable))) # Tipo 'NoType' cuando se juntan muchos tipos