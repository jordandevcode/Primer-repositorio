#a)	Crear una primera lista que parta con tres elementos y mostrarla.
lista_1 = ["Adidas", "Nike", "Reebok"]
print(lista_1)
#b)	Crear una segunda lista vacía y colocarle un nombre acorde a la temática que le corresponde trabajar.
MarcaZapatillas = []
#c)	Mostrar la lista vacía recién creada (usando print(), sin recorrerla con ciclo).
print(MarcaZapatillas)
#d)	Añadir uno a uno (usando ciclo for y el método append())  al menos siete (7) elementos en la lista vacía, todos deben quedar guardados con inicial en mayúscula. Debe solicitar al usuario cada elemento. (Recuerde uso de método capitalize()).
for i in range(7):
    zapatilla = input("Escribe una marca de zapatilla: ").capitalize()
    MarcaZapatillas.append(zapatilla)
#e)	Unir las dos listas en una sola (use operador para concatenar).
NuevaLista = lista_1 + MarcaZapatillas
#f)	Recorrer la lista final por valor y no por índice (usando un ciclo for) e ir mostrando uno a uno los elementos.
for i in NuevaLista:
    print(i)
#g)	Cambiar los dos (2) últimos elementos de la lista final por valores que Ud. defina (no pedidos por teclado).
NuevaLista[9]= "Puma"
NuevaLista[8]= "Skechers"
print(NuevaLista)
#h)	Pedir desde teclado al usuario un (1) elemento para añadirlo en la penúltima posición de la lista final (Considere uso de insert() y capitalize()).
MarcaNueva = input("Ingresa una marca de zapatilla nueva: ").capitalize()
NuevaLista.insert(9,MarcaNueva)
print(NuevaLista)
#i)	Eliminar tres (3) elementos de la lista final que Ud. defina (use para la primera eliminación el método del, para la segunda el método pop y para tercero el método remove).
del NuevaLista[0]
NuevaLista.pop(1)
NuevaLista.remove("Puma")
#j)	Mostrar nuevamente la lista final con todos los elementos (mediante print() sin recorrerla).
print(NuevaLista)
#k)	Obtener y mostrar el total de elementos que posee la lista final hasta ahora (use la función len()).
elementos = (len(NuevaLista))
print(f"El numero total de elementos que posee la lista es de {elementos}")
#l)	Ordenar la lista final de manera alfabética (Sugerencia: use el método sort()).
NuevaLista.sort()
#m)	Invertir la lista final (Sugerencia: use el método reverse()).
NuevaLista.reverse()
#n)	Mostrar nuevamente la lista final con todos los elementos (mediante print() sin recorrerla).
print(NuevaLista)
#o)	Pedir al usuario un elemento y mostrar cuantas veces aparece en la lista final (use el método count()).
element = input("Eliga un elemento para buscar en la lista: ").capitalize()
print(NuevaLista.count(element))
#p)	Crear una (1) función que permita buscar un elemento con uso de operador in, la función debe tener el formato:
def buscarElemento(elem,lista):
        if elem in lista:
            print("El elemento esta en la lista")
        else:
            print("El elemento no esta en la lista")
#q)	Generar una lista rebanada considerando del inicio al tercer elemento y mostrar la lista rebanada
rebanadalista = NuevaLista [:3]
print(rebanadalista)