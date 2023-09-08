import libro as l
import os

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros: 
        print(f"{libro['cod']} | {libro['titulo']} | Ejemplares prestados: {libro['cant_ej_pr']}")
    return None

def registrar_nuevo_libro():
    print("nuevo_libro")
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print(nuevo_libro)
    print("nuevo_libro")
    print(libros)
    return nuevo_libro

def eliminar_ejemplar_libro():
    codigo = input('Ingrese el codigo del libro que desea eliminar')
    for libro in libros: 
        if libro['cod'] == codigo: 
            print(f"La cantidad de libros antes de eliminar es {libro['cant_ej_ad']}")
            libro['cant_ej_ad'] -= 1 
            print(f"Libro eliminado con exito, la cantidad de libros de {libro['titulo']} actualizada es: {libro['cant_ej_ad']}")
            return None
        
    print("El codigo ingresado no existe")
    return None

def prestar_ejemplar_libro():
 #Retorno los libros si existen sino mostramos que no hay
    rs = verStockLibros()
    bandera = False
    if rs == True:
        opt = input("\nIngrese el codigo del libro:")
        #Recorremos todos los libros y verificamos que exista y tenga ejemplares para prestar
        for libro in libros: 
            if libro['cod'] == opt: 
                bandera = True
                if libro['cant_ej_ad'] < 1:
                    print(f'El libro no tiene ejemplares para prestar.')
                else: 
                    confirmacion = input(f'\nLibro que desea prestar: {libro["titulo"]} - {libro["autor"]} - {libro["cant_ej_ad"]}\n Escriba CANCELAR para volver atras, para confirmar presione Enter')
                    if confirmacion != 'CANCELAR':
                        libro['cant_ej_ad'] -= 1
                        libro['cant_ej_pr'] += 1
                        os.system ("cls")
                        print(f'Prestamo confirmado. Ingrese una opcion para seguir operando')
        if bandera == False:
             print('No se han encontro libros con ese codigo')
    return bandera
    
def verStockLibros():
    stockLibros = False
    for libro in libros:
        if libro['cant_ej_ad']>0:
            stockLibros = True
            print("Codigo: ", libro["cod"], "|" ,"Nombre: ", libro["titulo"],"|" , "Autor: ",libro["autor"],"|" ,"Cantidad de ejemplares: " ,libro["cant_ej_ad"],"|" ,"Cantidad de ejemplares prestados: ", libro["cant_ej_pr"])
        if not stockLibros:
            print("No hay libros disponibles")
    return stockLibros
   


def devolver_ejemplar_libro():
    codigo = input("Ingrese el codigo del libro a devolver")
    for libro in libros:
        if libro['cod'] == codigo: 
            if libro['cant_ej_pr'] >= 1:
                print("Se realizó la devolución correctamente!")
                libro['cant_ej_pr'] -= 1
            else: 
                print("No tiene ejemplares prestados!")
            return None
        print("El codigo ingresado no existe")
    return None

# def nuevo_libro():
#     #completar
#     return None