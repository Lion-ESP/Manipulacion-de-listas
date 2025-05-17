from validaciones import validar_lista_e_indice

def insertar(lista: list, elemento: any, indice: int) -> None:
    """
    insertar un elemento en una posicion especifica de la lista

    Modifica la lista original colocando elemento en la posicion indicada por indice.

    Parámetros:
    - lista (list): Lista a modificar.
    - elemento (any): Elemento a agregar al final.
    - indice (int): Indice donde colocar el elemento.

    Retorna:
    - None
    """
    if not validar_lista_e_indice(lista, indice, True):
        return
    
    longitud = len(lista)

    if indice >= longitud:
        lista[longitud:] = [elemento]
        return
    
    lista[longitud:] = [None]

    for i in range(longitud, indice, -1):
        lista[i] = lista[i-1]

    lista[indice] = elemento

# Caso de uso
if __name__ == "__main__":
    mi_lista = [10, 20, 30]
    print("Antes:", mi_lista)
    insertar(mi_lista, 4, 6)
    print("Después:", mi_lista) 