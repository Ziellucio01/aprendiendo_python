### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except 

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    # Se ejecuta si se produce una exceptión
    print("Se ha producido un error")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una exceptión
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre, pase lo que pase
    print("La ejecución continúa")
    
# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TyperError")

# Captura de la informacion de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)