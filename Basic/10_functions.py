### Funtions ###

from unittest import result


def my_funtion (): #funcion simple
    print("Esto es una función")

my_funtion ()
my_funtion ()
my_funtion ()

def sum_two_values (first_value: int, second_value): #funcion con parametros
    print(first_value +  second_value)

sum_two_values(5,7)
sum_two_values(54754,71231)
sum_two_values("5","7") #suma de strings se concatena
sum_two_values(1.4,5.2) #No podemos forsar el tipado ya que es dinamico

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10,5)
print(my_result)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure",name="Brais")

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")