# Ejercicio 1
# Creación de una función que retorna el mayor de 4 números enteros recibidos en sus parámetros. 


def funcion1(num1,num2,num3,num4):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    if num4 > max:
        max = num4
  
    return max



# Probar
res = funcion1(23,33,44,66)
print(res)