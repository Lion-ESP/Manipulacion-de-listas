from validaciones import validar_lista_y_elemento

def eliminar_todos(lista: list, elemento: any) -> None:
    """
    Eliminar todas las ocurrencias de un elemento en la lista.
    
    - Modificar la lista original, removiendo todos los elementos iguales al valor recibido.

    Parametros:
    - lista (list): lista a modificar.
    - elemento (any): elemento a eliminar de la lista.

    Retorna:
    - None.
    """
    if not validar_lista_y_elemento(lista, elemento):
        return
    
    new_list = []
    
    for item in lista:
        if item != elemento:
            new_list[len(new_list):] = [item]
    
    lista[:] = new_list


# Caso de uso
if __name__ == "__main__":
    mi_lista = [4, 8, 4, 4, 10]
    print("Antes:", mi_lista)
    eliminar_todos(mi_lista, 4)
    print("Después:", mi_lista) 
# Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].