from nodo import Nodo


class ListaCircularDoble:
    def __init__(self):
        self.actual = None  # nodo de la canción que "está sonando"
        self.tamano = 0  # cuántas canciones hay

    def esta_vacia(self):
        return self.actual is None

    def agregar(self, cancion):
        nuevo = Nodo(cancion)

        if self.esta_vacia():
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.actual = nuevo
        else:
            ultimo = self.actual.anterior

            ultimo.siguiente = nuevo  # la última ahora apunta al nuevo
            nuevo.anterior = ultimo  # el nuevo mira hacia atrás a la última
            nuevo.siguiente = self.actual  # el nuevo cierra el círculo hacia la actual
            self.actual.anterior = nuevo  # la actual ahora mira atrás al nuevo

        self.tamano += 1

    def siguiente(self):
        if self.esta_vacia():
            return
        self.actual = self.actual.siguiente

    def anterior(self):
        if self.esta_vacia():
            return
        self.actual = self.actual.anterior

    def a_lista(self):
        if self.esta_vacia():
            return []

        resultado = []
        nodo = self.actual
        for _ in range(self.tamano):
            resultado.append(nodo.cancion)
            nodo = nodo.siguiente
        return resultado

    def eliminar(self, cancion):
        if self.esta_vacia():
            return False

        nodo = self.actual
        for _ in range(self.tamano):
            if nodo.cancion == cancion:
                break
            nodo = nodo.siguiente
        else:
            return False
        
        if self.tamano == 1:
            self.actual = None
        else:
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior
            if nodo is self.actual:
                self.actual = nodo.siguiente

        self.tamano -= 1
        return True