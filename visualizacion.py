import os

ANCHO = 14  # ancho interior de cada caja


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def dibujar(canciones):
    limpiar_pantalla()
    if not canciones:
        print("(lista vacía)")
        return

    arriba = ""
    medio = ""
    abajo = ""
    for i, cancion in enumerate(canciones):
        es_ultima = (i == len(canciones) - 1)
        marca = "▶ " if i == 0 else "  "          # la primera es la que suena
        texto = (marca + cancion)[:ANCHO]          # recorta nombres largos
        espacio = "" if es_ultima else "     "
        flecha = "" if es_ultima else " ⇄   "

        arriba += "┌" + "─" * ANCHO + "┐" + espacio
        medio  += "│" + f"{texto:^{ANCHO}}" + "│" + flecha
        abajo  += "└" + "─" * ANCHO + "┘" + espacio

    print(arriba)
    print(medio)
    print(abajo)

    # Flecha que muestra que la última vuelve a la primera
    total = len(abajo)
    print(" ↑" + " " * (total - 3) + "│")
    print(" └" + " (vuelve al inicio) ".center(total - 3, "─") + "┘")


if __name__ == "__main__":
    dibujar(["Canción A", "Canción B", "Canción C"])