from validaciones import validar_lista_y_elemento

def obtener_indice(lista: list, elemento: any) -> int:
    """
    - Encontrar el índice de la primera ocurrencia de un elemento en la lista.

    Busca en la lista el elemento recibido y retornar su posición (índice).

    Parámetros:
    - lista (list): lista a evaluar
    - elemento (any): elemento a buscar su indice dentro de la lista.

    Retorna:
    Si el elemento no existe en la lista, retorna -1.
    """
    if not validar_lista_y_elemento(lista, elemento):
        return
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


# Caso de uso
if __name__ == "__main__":
    mi_lista = [10, 20, 30]
    print("Antes:", mi_lista)
    resultado = obtener_indice(mi_lista, 20)
    print("Resultado:", resultado) 