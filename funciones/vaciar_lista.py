from validaciones import validar_lista

def vaciar_lista(lista: list) -> None:
    """
    - Eliminar todos los elementos de la lista, dejándola vacía.
    
    Modifica la lista original, removiendo todos sus elementos.

    Parámetros: 
    - lista (list): lista a modificar.
    """
    if not validar_lista(lista):
        return
    
    lista[:] = []


if __name__ == "__main__":
    mi_lista = [1, 2, 3, 4, 5]
    print("Antes:", mi_lista)
    vaciar_lista(mi_lista)
    print("Después:", mi_lista) 
# Ejemplo: Si la lista es [1, 2, 3], al llamar a vaciar_lista(), la lista quedará [].
