from lista_circular import ListaCircularDoble

lista = ListaCircularDoble()

# Lista vacía: nada debe fallar
lista.siguiente()
lista.anterior()
lista.eliminar("X")
assert lista.a_lista() == []

# Un solo nodo se apunta a sí mismo
lista.agregar("A")
assert lista.a_lista() == ["A"]
lista.siguiente()
assert lista.a_lista() == ["A"]

# Vuelta completa hacia adelante
lista.agregar("B")
lista.agregar("C")
lista.siguiente(); lista.siguiente(); lista.siguiente()
assert lista.a_lista()[0] == "A"

# Retroceder desde la primera lleva a la última
lista.anterior()
assert lista.a_lista() == ["C", "A", "B"]
lista.siguiente()  # volvemos a A

# Eliminar la canción actual
lista.eliminar("A")
assert lista.a_lista() == ["B", "C"]
assert lista.tamano == 2

# Eliminar algo que no existe no cambia nada
lista.eliminar("Z")
assert lista.a_lista() == ["B", "C"]

# Vaciar la lista
lista.eliminar("B")
lista.eliminar("C")
assert lista.esta_vacia()
assert lista.a_lista() == []
assert lista.tamano == 0

print("Todas las pruebas pasaron ✅")