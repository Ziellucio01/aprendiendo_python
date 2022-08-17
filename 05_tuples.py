### Tuples ###

from traceback import print_tb


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35,60,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

#my_tuple[1] = 1.80 TypeError: 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)

print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] No podemos eliminar un elemento de la tupla

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined