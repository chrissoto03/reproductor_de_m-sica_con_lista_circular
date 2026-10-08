from lista_circular import ListaCircularDoble


def crear(*canciones):
    """Crea una lista con las canciones dadas, en ese orden."""
    lista = ListaCircularDoble()
    for c in canciones:
        lista.agregar(c)
    return lista


def prueba_lista_vacia():
    lista = ListaCircularDoble()
    lista.siguiente()                      # no debe fallar
    lista.anterior()                       # no debe fallar
    assert lista.eliminar("X") is False    # no debe fallar
    assert lista.a_lista() == []
    assert lista.esta_vacia()
    assert lista.tamano == 0


def prueba_un_solo_nodo():
    lista = crear("A")
    assert lista.a_lista() == ["A"]
    assert lista.actual.siguiente is lista.actual   # se apunta a sí mismo
    assert lista.actual.anterior is lista.actual
    lista.siguiente()
    assert lista.a_lista() == ["A"]
    lista.anterior()
    assert lista.a_lista() == ["A"]


def prueba_agregar_orden():
    lista = crear("A", "B", "C")
    assert lista.a_lista() == ["A", "B", "C"]
    assert lista.tamano == 3
    assert lista.actual.cancion == "A"     # agregar no cambia la que suena


def prueba_vuelta_completa_adelante():
    lista = crear("A", "B", "C")
    lista.siguiente()
    assert lista.a_lista() == ["B", "C", "A"]
    lista.siguiente()
    lista.siguiente()                      # pasó por la última y volvió a A
    assert lista.a_lista() == ["A", "B", "C"]


def prueba_vuelta_completa_atras():
    lista = crear("A", "B", "C")
    lista.anterior()                       # desde la primera, va a la última
    assert lista.a_lista() == ["C", "A", "B"]
    lista.anterior()
    lista.anterior()
    assert lista.a_lista() == ["A", "B", "C"]


def prueba_eliminar_actual():
    lista = crear("A", "B", "C")           # suena A
    assert lista.eliminar("A") is True
    assert lista.a_lista() == ["B", "C"]   # ahora suena B
    assert lista.tamano == 2


def prueba_eliminar_ultimo():
    lista = crear("A", "B", "C")
    assert lista.eliminar("C") is True
    assert lista.a_lista() == ["A", "B"]
    lista.siguiente()
    lista.siguiente()                      # el círculo se cerró bien
    assert lista.a_lista() == ["A", "B"]
    lista.anterior()
    assert lista.a_lista() == ["B", "A"]


def prueba_eliminar_medio():
    lista = crear("A", "B", "C")
    assert lista.eliminar("B") is True
    assert lista.a_lista() == ["A", "C"]
    assert lista.actual.siguiente.cancion == "C"
    assert lista.actual.anterior.cancion == "C"


def prueba_eliminar_no_actual_conserva_actual():
    lista = crear("A", "B", "C")
    lista.siguiente()                      # suena B
    lista.eliminar("C")
    assert lista.actual.cancion == "B"     # B sigue sonando
    assert lista.a_lista() == ["B", "A"]


def prueba_eliminar_inexistente():
    lista = crear("A", "B")
    assert lista.eliminar("Z") is False
    assert lista.a_lista() == ["A", "B"]
    assert lista.tamano == 2


def prueba_vaciar_y_reutilizar():
    lista = crear("A", "B", "C")
    lista.eliminar("A")
    lista.eliminar("B")
    lista.eliminar("C")
    assert lista.esta_vacia()
    assert lista.actual is None
    assert lista.tamano == 0
    assert lista.a_lista() == []
    lista.agregar("N")                     # debe funcionar de nuevo
    assert lista.a_lista() == ["N"]


if __name__ == "__main__":
    pruebas = [
        prueba_lista_vacia,
        prueba_un_solo_nodo,
        prueba_agregar_orden,
        prueba_vuelta_completa_adelante,
        prueba_vuelta_completa_atras,
        prueba_eliminar_actual,
        prueba_eliminar_ultimo,
        prueba_eliminar_medio,
        prueba_eliminar_no_actual_conserva_actual,
        prueba_eliminar_inexistente,
        prueba_vaciar_y_reutilizar,
    ]
    for prueba in pruebas:
        prueba()
        print(f"✅ {prueba.__name__}")
    print("\nTodas las pruebas pasaron ✅")