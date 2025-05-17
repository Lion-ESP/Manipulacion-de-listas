from validaciones import validar_lista

def eliminar(lista: list) -> int:
    """
    - Eliminar el úlitmo elemento de la lista y retornarlo.

    Modificar la lista original, removiendo su último elemento.

    Parámetros:
    - lista (list): lista a modificar.

    Retorna:
    - El elemento eliminado (int).
    """
    if not validar_lista(lista):
        return
    
    elemento_eliminado = lista[-1]

    lista[:] = lista[:-1]

    return elemento_eliminado


# Caso de uso
if __name__ == "__main__":
    mi_lista = [10, 20, 30]
    print("Antes:", mi_lista)
    resultado = eliminar(mi_lista)
    print("Resultado:", resultado) 
    print("Despues:", mi_lista)