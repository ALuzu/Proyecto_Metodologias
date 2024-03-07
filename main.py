import tkinter as tk
from tkinter import messagebox

class Transaction:
    def __init__(self, date, amount, transaction_type, category, payment_method, description):
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.payment_method = payment_method
        self.description = description

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        messagebox.showinfo("Éxito", "Transacción registrada correctamente.")

class UserInterface(tk.Tk):
    def __init__(self, transaction_manager):
        super().__init__()
        self.title("Gestión Financiera Familiar")
        self.geometry("400x200")

        self.transaction_manager = transaction_manager

        self.label = tk.Label(self, text="¡Bienvenido a la aplicación de gestión financiera!")
        self.label.pack(pady=10)

        self.button_transactions = tk.Button(self, text="Registrar Transacción", command=self.register_transaction)
        self.button_transactions.pack(pady=5)

    def register_transaction(self):
        transaction_window = tk.Toplevel(self)
        transaction_window.title("Registrar Transacción")
        transaction_window.geometry("300x200")

        label_date = tk.Label(transaction_window, text="Fecha:")
        label_date.grid(row=0, column=0)
        entry_date = tk.Entry(transaction_window)
        entry_date.grid(row=0, column=1)

        label_amount = tk.Label(transaction_window, text="Monto:")
        label_amount.grid(row=1, column=0)
        entry_amount = tk.Entry(transaction_window)
        entry_amount.grid(row=1, column=1)

        label_type = tk.Label(transaction_window, text="Tipo:")
        label_type.grid(row=2, column=0)
        entry_type = tk.Entry(transaction_window)
        entry_type.grid(row=2, column=1)

        label_category = tk.Label(transaction_window, text="Categoría:")
        label_category.grid(row=3, column=0)
        entry_category = tk.Entry(transaction_window)
        entry_category.grid(row=3, column=1)

        label_payment_method = tk.Label(transaction_window, text="Método de Pago:")
        label_payment_method.grid(row=4, column=0)
        entry_payment_method = tk.Entry(transaction_window)
        entry_payment_method.grid(row=4, column=1)

        label_description = tk.Label(transaction_window, text="Descripción:")
        label_description.grid(row=5, column=0)
        entry_description = tk.Entry(transaction_window)
        entry_description.grid(row=5, column=1)

        register_button = tk.Button(transaction_window, text="Registrar", command=lambda: self.register_entry(entry_date.get(), entry_amount.get(), entry_type.get(), entry_category.get(), entry_payment_method.get(), entry_description.get()))
        register_button.grid(row=6, columnspan=2)

    def register_entry(self, date, amount, transaction_type, category, payment_method, description):
        if not all([date, amount, transaction_type, category, payment_method]):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        new_transaction = Transaction(date, amount, transaction_type, category, payment_method, description)
        self.transaction_manager.add_transaction(new_transaction)

def main():
    transaction_manager = TransactionManager()
    app = UserInterface(transaction_manager)
    app.mainloop()

if __name__ == "__main__":
    main()
