### Strings ###
print("### Strings ###")

my_string = "My String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

# Formateo 
name, surname, age = "Raziel", "Lucio", 31
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))


print("Mi nombre es "+  name + " " + surname +" y mi edad es " + str(age)) 
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetando de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

# Reverse -> para retos de programación

reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")