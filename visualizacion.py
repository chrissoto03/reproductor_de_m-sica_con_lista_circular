import tkinter as tk
from lista_circular import ListaCircularDoble

ANCHO_TOTAL = 860
SEPARACION = 40
ALTO_CAJA = 50
Y_CAJA = 60


class App:
    def __init__(self, raiz):
        self.lista = ListaCircularDoble()
        raiz.title("Reproductor circular")

        self.canvas = tk.Canvas(raiz, width=900, height=240, bg="white")
        self.canvas.pack(padx=10, pady=10)

        panel = tk.Frame(raiz)
        panel.pack(pady=5)
        self.entrada = tk.Entry(panel, width=25)
        self.entrada.grid(row=0, column=0, padx=5)
        self.entrada.bind("<Return>", lambda e: self.agregar())
        tk.Button(panel, text="Agregar", command=self.agregar).grid(row=0, column=1, padx=3)
        tk.Button(panel, text="Eliminar", command=self.eliminar).grid(row=0, column=2, padx=3)
        tk.Button(panel, text="⏮ Anterior", command=self.anterior).grid(row=0, column=3, padx=3)
        tk.Button(panel, text="⏭ Siguiente", command=self.siguiente).grid(row=0, column=4, padx=3)

        self.mensaje = tk.Label(raiz, text="")
        self.mensaje.pack(pady=5)
        self.redibujar()

    # ---- acciones: cada una modifica la lista y luego redibuja ----
    def agregar(self):
        nombre = self.entrada.get().strip()
        if not nombre:
            self.mensaje.config(text="Escriba un nombre.")
            return
        self.lista.agregar(nombre)
        self.entrada.delete(0, "end")
        self.mensaje.config(text=f"Se agregó '{nombre}'.")
        self.redibujar()

    def eliminar(self):
        nombre = self.entrada.get().strip()
        if self.lista.eliminar(nombre):
            self.mensaje.config(text=f"Se eliminó '{nombre}'.")
            self.entrada.delete(0, "end")
        else:
            self.mensaje.config(text=f"No se encontró '{nombre}'.")
        self.redibujar()

    def siguiente(self):
        self.lista.siguiente()
        self.redibujar()

    def anterior(self):
        self.lista.anterior()
        self.redibujar()

    # ---- dibujo ----
    def redibujar(self):
        self.canvas.delete("all")
        canciones = self.lista.a_lista()
        n = len(canciones)
        if n == 0:
            self.canvas.create_text(450, 120, text="(lista vacía)", font=("Arial", 14))
            return

        ancho = min(120, (ANCHO_TOTAL - (n - 1) * SEPARACION) / n)
        x0 = (900 - (n * ancho + (n - 1) * SEPARACION)) / 2

        centros = []
        for i, cancion in enumerate(canciones):
            x = x0 + i * (ancho + SEPARACION)
            color = "#a8e6a1" if i == 0 else "#e8e8e8"   # verde = la que suena
            self.canvas.create_rectangle(x, Y_CAJA, x + ancho, Y_CAJA + ALTO_CAJA,
                                         fill=color, outline="black", width=2)
            texto = ("▶ " if i == 0 else "") + cancion
            self.canvas.create_text(x + ancho / 2, Y_CAJA + ALTO_CAJA / 2,
                                    text=texto, width=ancho - 8, font=("Arial", 10))
            centros.append(x + ancho / 2)
            if i < n - 1:   # flecha doble entre cajas
                y = Y_CAJA + ALTO_CAJA / 2
                self.canvas.create_line(x + ancho, y, x + ancho + SEPARACION, y,
                                        arrow=tk.BOTH, width=2)

        # flecha que cierra el círculo: última -> primera
        y_base = Y_CAJA + ALTO_CAJA
        if n > 1:
            y_baja = y_base + 50
            self.canvas.create_line(centros[-1], y_base, centros[-1], y_baja,
                                    centros[0], y_baja, centros[0], y_base,
                                    arrow=tk.LAST, width=2, fill="#c0392b")
            self.canvas.create_text((centros[0] + centros[-1]) / 2, y_baja + 15,
                                    text="la última vuelve a la primera",
                                    fill="#c0392b")
        else:
            self.canvas.create_text(centros[0], y_base + 25,
                                    text="un solo nodo: se apunta a sí mismo",
                                    fill="#c0392b")


if __name__ == "__main__":
    raiz = tk.Tk()
    App(raiz)
    raiz.mainloop()