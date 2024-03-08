import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Transaccion:
    def __init__(self, fecha, monto, tipo_transaccion, categoria, metodo_pago, descripcion):
        self.fecha = fecha
        self.monto = monto
        self.tipo_transaccion = tipo_transaccion
        self.categoria = categoria
        self.metodo_pago = metodo_pago
        self.descripcion = descripcion

class AdministradorTransacciones:
    def __init__(self):
        self.transacciones = []
        self.monto_total = 0

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)
        self.transacciones.sort(key=lambda x: datetime.strptime(x.fecha, "%d/%m/%Y"))
        if transaccion.tipo_transaccion == "Ingreso":
            self.monto_total += transaccion.monto
        else:
            self.monto_total -= transaccion.monto

class InterfazUsuario(tk.Tk):
    def __init__(self, administrador_transacciones):
        super().__init__()
        self.title("Gestión Financiera Familiar")
        self.geometry("800x400")

        self.administrador_transacciones = administrador_transacciones

        self.etiqueta = tk.Label(self, text="¡Bienvenido a la aplicación de gestión financiera!")
        self.etiqueta.pack(pady=10)

        self.etiqueta_monto_total = tk.Label(self, text=f"Monto Total: {self.administrador_transacciones.monto_total}")
        self.etiqueta_monto_total.pack(pady=5)

        self.boton_registrar = tk.Button(self, text="Registrar Transacción", command=self.registrar_transaccion)
        self.boton_registrar.pack(pady=5)

        self.boton_historial = tk.Button(self, text="Ver Historial de Transacciones", command=self.ver_historial)
        self.boton_historial.pack(pady=5)

    def registrar_transaccion(self):
        ventana_transaccion = tk.Toplevel(self)
        ventana_transaccion.title("Registrar Transacción")
        ventana_transaccion.geometry("300x250")

        label_fecha = tk.Label(ventana_transaccion, text="Fecha (DD/MM/AAAA):")
        label_fecha.grid(row=0, column=0)
        entry_fecha = tk.Entry(ventana_transaccion)
        entry_fecha.grid(row=0, column=1)

        label_monto = tk.Label(ventana_transaccion, text="Monto:")
        label_monto.grid(row=1, column=0)
        entry_monto = tk.Entry(ventana_transaccion)
        entry_monto.grid(row=1, column=1)

        label_tipo = tk.Label(ventana_transaccion, text="Tipo de Transacción:")
        label_tipo.grid(row=2, column=0)
        opciones_tipo = ["Ingreso", "Gasto"]
        seleccion_tipo = tk.StringVar(ventana_transaccion)
        seleccion_tipo.set(opciones_tipo[0])  # Por defecto, selecciona Ingreso
        menu_tipo = tk.OptionMenu(ventana_transaccion, seleccion_tipo, *opciones_tipo)
        menu_tipo.grid(row=2, column=1)

        label_categoria = tk.Label(ventana_transaccion, text="Categoría:")
        label_categoria.grid(row=3, column=0)
        entry_categoria = tk.Entry(ventana_transaccion)
        entry_categoria.grid(row=3, column=1)

        label_metodo_pago = tk.Label(ventana_transaccion, text="Método de Pago:")
        label_metodo_pago.grid(row=4, column=0)
        entry_metodo_pago = tk.Entry(ventana_transaccion)
        entry_metodo_pago.grid(row=4, column=1)

        label_descripcion = tk.Label(ventana_transaccion, text="Descripción:")
        label_descripcion.grid(row=5, column=0)
        entry_descripcion = tk.Entry(ventana_transaccion)
        entry_descripcion.grid(row=5, column=1)

        boton_registrar = tk.Button(ventana_transaccion, text="Registrar", command=lambda: self.registrar_entrada(entry_fecha.get(), entry_monto.get(), seleccion_tipo.get(), entry_categoria.get(), entry_metodo_pago.get(), entry_descripcion.get(), ventana_transaccion))
        boton_registrar.grid(row=6, columnspan=2, pady=5)

    def registrar_entrada(self, fecha, monto, tipo, categoria, metodo_pago, descripcion, ventana):
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            monto = float(monto)
            nueva_transaccion = Transaccion(fecha, monto, tipo, categoria, metodo_pago, descripcion)
            self.administrador_transacciones.agregar_transaccion(nueva_transaccion)
            self.actualizar_monto_total()
            messagebox.showinfo("Éxito", "Transacción registrada correctamente")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una fecha válida y un monto numérico.")

    def actualizar_monto_total(self):
        self.etiqueta_monto_total.config(text=f"Monto Total: {self.administrador_transacciones.monto_total}")

    def ver_historial(self):
        historial_window = tk.Toplevel(self)
        historial_window.title("Historial de Transacciones")
        historial_window.geometry("800x400")

        tabla = ttk.Treeview(historial_window)

        tabla["columns"] = ("Fecha", "Monto", "Tipo", "Categoría", "Método de Pago", "Descripción")
        tabla.heading("#0", text="Nro.")
        tabla.heading("Fecha", text="Fecha")
        tabla.heading("Monto", text="Monto")
        tabla.heading("Tipo", text="Tipo")
        tabla.heading("Categoría", text="Categoría")
        tabla.heading("Método de Pago", text="Método de Pago")
        tabla.heading("Descripción", text="Descripción")

        tabla.column("#0", width=50)
        tabla.column("Fecha", width=100)
        tabla.column("Monto", width=70)
        tabla.column("Tipo", width=70)
        tabla.column("Categoría", width=100)
        tabla.column("Método de Pago", width=100)
        tabla.column("Descripción", width=200)

        for idx, transaccion in enumerate(self.administrador_transacciones.transacciones, start=1):
            tabla.insert("", "end", text=idx, values=(transaccion.fecha, transaccion.monto, transaccion.tipo_transaccion, transaccion.categoria, transaccion.metodo_pago, transaccion.descripcion))

        tabla.pack(padx=10, pady=10)

        etiqueta_total = tk.Label(historial_window, text=f"Monto Total: {self.administrador_transacciones.monto_total}")
        etiqueta_total.pack(side="bottom", pady=5)

def main():
    administrador_transacciones = AdministradorTransacciones()
    app = InterfazUsuario(administrador_transacciones)
    app.mainloop()

if __name__ == "__main__":
    main()

