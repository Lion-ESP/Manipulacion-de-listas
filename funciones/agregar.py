from validaciones import validar_lista_y_elemento

def agregar(lista: list, elemento: any) -> None:
    """
    Agrega un elemento al final de la lista

    Modifica la lista original agregando el elemento como último.

    Parámetros:
    - lista (list): Lista a modificar.
    - elemento (any): Elemento a agregar al final.

    Retorna:
    - None
    """
    if not validar_lista_y_elemento(lista, elemento):
        return
    
    lista[len(lista):] = [elemento]

# Caso de uso
if __name__ == "__main__":
    mi_lista = [1, 2, 3]
    print("Antes:", mi_lista)
    agregar(mi_lista, 4)
    print("Después:", mi_lista) 