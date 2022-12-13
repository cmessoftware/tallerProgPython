# Ejercicio 4

# Realice un programa que muestre un menú con las 4 opciones siguientes:
# 1. Área de un Triángulo equilátero  --> L*L/2
# 2. Área de un rombo (basado en las medidas de su diagonal mayor y diagonal menor)
# 3. Volumen de un cubo.
# 4. Salir
# Para cada una de las 3 primeras opciones del menú anterior, debe crear una función diferente para resolver el cálculo correspondiente.
# Validar los datos del menú.

# Asumo que los valores ingresados son numeros enteros.


def menu():

    while 1:
        opcion = input("Ingrese opcion ")

        if (opcion == '1'):
            L = input("Ingrese Lado del triangulo equilatero: ")
            if validar(L) == True:
                area = area_triagulo_eq(int(L))
            else:
                print(f"El valor de L: {L} es incorrecto")
                continue    

            print(f"El area del triangulo equiletero de {L} cm es {area}")

        if (opcion == '2'):
            l = input("Ingrese diagonal menor del rombo: ")
            L = input("Ingrese diagonal mayor del rombo: ")

            if validar(l) and  validar(L):
                area = area_rombo(int(l), int(L))
            else:
                print(f"El valor de l: {l} o L: {L} es incorrecto")
                continue    
        
            print(f"El area del rombo de digonal menor {l} cm y mayor {L} cm es {area}")

        if (opcion == '3'):
            L = input("Ingrese lado cubo: ")
            if validar(L):
                vol = volumen_cubo(int(L))
            else:
                print(f"El valor de L: {L} es incorrecto")
                continue    

            print(f"El volumen del cubo de {L} cm de lado  es {vol}")

        if (opcion == '4'):
            print("Chau")
            break


# Valido que L es un numero 
def validar(L):
    return L.isnumeric()
     


def area_triagulo_eq(L):
    return L*L/2


def area_rombo(l, L):
    return (l*L-l*l)/2


def volumen_cubo(L):
    return pow(L, 3)  # L*L*L


# Probamos
menu()
