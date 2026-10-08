from nodo import Nodo


class ListaCircularDoble:
    def __init__(self):
        self.actual = None   # nodo de la canción que "está sonando"
        self.tamano = 0      # cuántas canciones hay

    def esta_vacia(self):
        return self.actual is None

    def agregar(self, cancion):         # Persona A
        pass

    def siguiente(self):                # Persona A
        pass

    def anterior(self):                 # Persona A
        pass

    def a_lista(self):                  # Persona A
        pass

    def eliminar(self, cancion):        # Persona B
        # Caso 1: lista vacía → no hacer nada
        if self.esta_vacia():
            return

        # Caso 2: buscar el nodo dando una sola vuelta
        nodo = self.actual
        encontrado = False
        for _ in range(self.tamano):
            if nodo.cancion == cancion:
                encontrado = True
                break
            nodo = nodo.siguiente

        if not encontrado:
            return  # la canción no existe

        # Caso 3: era el único nodo → la lista queda vacía
        if self.tamano == 1:
            self.actual = None
            self.tamano = 0
            return

        # Caso 4: hay más nodos → los vecinos se apuntan entre sí y se saltan este nodo
        nodo.anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = nodo.anterior

        # Si borré la que estaba sonando, paso a la siguiente
        if nodo is self.actual:
            self.actual = nodo.siguiente

        self.tamano -= 1