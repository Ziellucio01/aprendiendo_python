### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Moredev")

print(my_other_set) # Un set no es una estructura ordena

my_other_set.add("Moredev") # Un set no admite repetidos

print(my_other_set)