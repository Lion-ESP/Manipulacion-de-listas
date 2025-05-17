def validar_lista(lista: list) -> bool:
    """
    Verifica que la variable sea una lista.

    Parámetros:
    - lista (list): Objeto a verificar.

    Retorna:
    - bool: True si es una lista, False si no lo es.
    """
    if type(lista) != list:
        print("Error: no es una lista válida.")
        return False
    return True

def validar_lista_e_indice(lista: list, indice: int) -> bool:
    """
    Valida una lista y un índice combinados.

    Parámetros:
    - lista (list): Lista a verificar.
    - indice (int): Índice a verificar.

    Retorna:
    - bool: True si ambos son válidos.
    """
    if not validar_lista(lista):
        return False
    
    if type(indice) != int:
        print("Error: el índice no es un número entero.")
        return False
    return True

def validar_lista_y_elemento(lista: list, elemento: any) -> bool:
    """
    Valida una lista y un elemento (la validación del elemento es mínima).

    Parámetros:
    - lista (list): Lista a verificar.
    - elemento (any): Elemento a verificar.

    Retorna:
    - bool: True si la lista es válida.
    """
    return validar_lista(lista)
