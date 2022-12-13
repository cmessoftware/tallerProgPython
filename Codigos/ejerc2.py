# Ejercicios 2

# Desarrolle una aplicación que solicite 2 números enteros al usuario, para que le muestre la resta y la división entre ambos valores.
# Esta aplicación debe tener tres funciones: ingreso de datos, resta y división.


def ingrese_datos():
    num1 = input("Ingrese 1 numero")  
    num2 = input("Ingrese 1 numero")  
    return (num1,num2)
    

def resta(num1,num2):
    return num1 - num2


def division(num1,num2):
    return num1 / num2



# Prueba

(num1,num2) = ingrese_datos()

resultado = resta(int(num1),int(num2))
print(resultado)

resultado = division(int(num1),int(num2))
print(resultado)
