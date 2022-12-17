# Usando el algoritmo de ordenamientp or burbuja ordenar el siguiente array
# numeros[] = [5,2,4,1,3]


def ordenar(lista):
    n = 0
    l = len(lista)
    flag = 0
    while l != 0:
        for i in range(1,l):
            if lista[i-1]>lista[i]:
                aux = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = aux
                n = i
                flag = 1
                mostrar_lista(lista)
        
        if flag:
            l = n
        else:
            l = 0
   		
                
def mostrar_lista(lista):
    for i in range(0,len(lista)):
        print(lista[i])
    print("**************************")



lista = []
lista = [5,2,4,1,3,66,77,-2,3,5,7,2,0,90,-8.-9-56,99,40,33,22,11,44,23,1,16]

ordenar(lista)





    