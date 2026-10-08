
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion    # el nombre de la canción
        self.siguiente = None     # a quién apunta hacia adelante
        self.anterior = None      # a quién apunta hacia atrás