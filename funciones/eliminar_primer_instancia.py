from obtener_indice import obtener_indice
from validaciones import validar_lista_y_elemento

def eliminar_primer_instancia(lista: list, elemento: any):
    """
    - Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.

    Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.

    Parámetros:
    - lista (list): lista a modificar.
    - elemento (any): elemento a eliminar.

    Retorna:
    - El elemento eliminado (int).
    - Si no existe se retorna None.
    """
    if not validar_lista_y_elemento(lista, elemento):
        return
    indice = obtener_indice(lista, elemento)

    if indice == -1:
        return False
    
    for i in range(indice, len(lista) -1):
        lista[i] = lista[i + 1]
    
    lista[:] = lista[:-1]

    return True


# Caso de uso
if __name__ == "__main__":
    mi_lista = [5, 3, 5, 7]
    print("Antes:", mi_lista)
    resultado = eliminar_primer_instancia(mi_lista, 5)
    print("Resultado:", resultado)
    print("Después:", mi_lista) 
    
    resultado = eliminar_primer_instancia(mi_lista, 5)
    print("Resultado:", resultado)
    print("Después:", mi_lista) 