# Ejercicio 5

# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 1 y 10). 
# A continuación debe mostrar todas las notas, el promedio, la nota más alta que ha sacado y la menor.


def menu():
    CANTIDAD = 5
    notas = []

    for i in range(CANTIDAD):
        while 1:
            nota = input("Ingrese nota ")
            if not validar(nota):
                print(f"El valor de nota {nota} es incorrecto")
                continue
            else:
                notas.append(nota)
                break
                
 
    mostrar_notas(notas)

    prom = promedio(notas)
    print(f"El promedio de las {CANTIDAD} notas es {prom}")

    max = nota_mayor(notas)
    print(f"La nota mayor de las {CANTIDAD} notas es {max}")

    min = nota_menor(notas)
    print(f"La nota menor de las {CANTIDAD} notas es {min}")


# Funciones

def validar(nota):
    return (nota.isnumeric() and  int(nota) >= 1 and int(nota) <= 10)


def mostrar_notas(notas):
    for n in notas:
        print(f"Nota: {n}")

def promedio(notas):
    sum = 0
    for n in notas:
        sum = sum + int(n)

    prom = sum/len(notas)
    return prom


def nota_mayor(notas):
    max = 0
    for n in notas:
        if int(n) > max:
            max = int(n)
    return max

def nota_menor(notas):
    min = 11
    for n in notas:
        if int(n) < min:
            min = int(n)
    return min


# Probando
menu()    

    
    
