# Reproductor "repetir todo"

**Caso elegido:** Caso 2, reproductor con siguiente/anterior y vuelta automática.

**Variante usada:** lista circular doblemente enlazada.

## Justificación
- Circular: el `siguiente` de la última apunta a la primera, y el `anterior`
  de la primera apunta a la última. Por eso `siguiente()` y `anterior()` son
  una sola línea, sin `if` de "llegué al final".
- Doble: retroceder es un solo paso con `.anterior`.

## Por qué no las otras
- Simple: retroceder obliga a recorrer desde el inicio, y al llegar al final
  hay que tratar el caso especial de volver al principio.
- Circular simple: avanzar es fácil, pero retroceder es costoso.
- Doble no circular: ambos sentidos funcionan, pero en los dos extremos
  hay que escribir casos especiales.
- (Completen con lo que vieron en el cuadro comparativo de la Sesión 3.)

## Costo
Cada nodo guarda un puntero extra (`anterior`), a cambio de simplificar el código.

## Cómo ejecutar
python main.py        # programa
python pruebas.py     # pruebas
