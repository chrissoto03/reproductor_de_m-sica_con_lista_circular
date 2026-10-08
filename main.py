from lista_circular import ListaCircularDoble
from visualizacion import dibujar

MENU = """
1. Agregar canción
2. Eliminar canción
3. Siguiente ⏭
4. Anterior ⏮
0. Salir
"""


def main():
    lista = ListaCircularDoble()
    mensaje = "Bienvenido. Agregue canciones para empezar."

    while True:
        dibujar(lista.a_lista())
        print(f"\n{mensaje}")
        print(MENU)
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la canción: ").strip()
            if nombre:
                lista.agregar(nombre)
                mensaje = f"Se agregó '{nombre}'."
            else:
                mensaje = "El nombre no puede estar vacío."
        elif opcion == "2":
            nombre = input("Canción a eliminar: ").strip()
            if lista.eliminar(nombre):
                mensaje = f"Se eliminó '{nombre}'."
            else:
                mensaje = f"No se encontró '{nombre}'."
        elif opcion == "3":
            lista.siguiente()
            mensaje = "Pasó a la siguiente."
        elif opcion == "4":
            lista.anterior()
            mensaje = "Volvió a la anterior."
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            mensaje = "Opción no válida."


if __name__ == "__main__":
    main()