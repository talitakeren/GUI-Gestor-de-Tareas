import tkinter as tk
from tkinter import messagebox, ttk
from src.logica.gestor_tareas import GestorTareas, Tarea

class GestorTareasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x350")
        self.root.configure(bg="#f7f7f7")

        # Crear una instancia de GestorTareas
        self.gestor = GestorTareas()

        # Frame para los campos de entrada
        input_frame = tk.Frame(root, bg="#f7f7f7")
        input_frame.pack(pady=10)

        # Etiqueta y entrada para el título
        self.title_label = tk.Label(input_frame, text="Título de la tarea:", bg="#f7f7f7", font=("Arial", 10, "bold"))
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.title_entry = tk.Entry(input_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para la descripción
        self.desc_label = tk.Label(input_frame, text="Descripción de la tarea:", bg="#f7f7f7", font=("Arial", 10, "bold"))
        self.desc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.desc_entry = tk.Entry(input_frame, width=40)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón para agregar tarea
        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.add_button.pack(pady=10)

        # Tabla (Treeview) para mostrar las tareas
        self.task_table = ttk.Treeview(root, columns=("Numero", "Titulo", "Descripcion"), show="headings", height=8)
        self.task_table.heading("Numero", text="N°")
        self.task_table.heading("Titulo", text="Título")
        self.task_table.heading("Descripcion", text="Descripción")

        self.task_table.column("Numero", width=50, anchor="center")
        self.task_table.column("Titulo", width=150, anchor="center")
        self.task_table.column("Descripcion", width=250, anchor="center")

        self.task_table.pack(pady=10)

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if not title:
            messagebox.showwarning("Advertencia", "El título no puede estar vacío")
            return

        try:
            # Agregar tarea al gestor
            self.gestor.agregar_tarea(title, description)
            # Obtener el número de la tarea
            task_number = len(self.gestor.tareas)
            # Agregar tarea a la tabla
            self.task_table.insert("", "end", values=(task_number, title, description))
            # Limpiar campos de entrada
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasGUI(root)
    root.mainloop()