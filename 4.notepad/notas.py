import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("700x420")
        self.archivo_actual = None
        self.modificado = False

        # Fuente por defecto
        self.fuente_actual = font.Font(family="Consolas", size=13)

        # Frame para margen y área texto
        self.text_frame = tk.Frame(self)
        self.text_frame.pack(expand=True, fill=tk.BOTH)

        # Margen numeración de líneas
        self.lineas = tk.Text(self.text_frame, width=4, padx=4, takefocus=0, border=0,
                            background="#e8e8e8", foreground="#555", state="disabled",
                            font=self.fuente_actual)
        self.lineas.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto
        self.text_area = tk.Text(self.text_frame, undo=True, wrap=tk.WORD, font=self.fuente_actual)
        self.text_area.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.text_area.bind("<<Modified>>", self.on_modificado)
        self.text_area.bind('<KeyRelease>', lambda e: self.actualizar_numeros())
        self.text_area.bind('<MouseWheel>', lambda e: self.actualizar_numeros())
        self.text_area.bind('<ButtonRelease-1>', lambda e: self.actualizar_numeros())
        self.text_area.bind('<Configure>', lambda e: self.actualizar_numeros())
        
        # Scrollbar
        self.scroll = tk.Scrollbar(self.text_frame, command=self.scroll_todo, orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area['yscrollcommand'] = self.on_scroll
        self.lineas['yscrollcommand'] = self.scroll.set

        self.crear_menu()
        self.protocol("WM_DELETE_WINDOW", self.preguntar_cerrar)
        self.actualizar_numeros()

    def crear_menu(self):
        menubar = tk.Menu(self)
        # Archivo
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como...", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.preguntar_cerrar)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        # Editar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar", command=lambda: self.text_area.event_generate("<<Cut>>"))
        editmenu.add_command(label="Copiar", command=lambda: self.text_area.event_generate("<<Copy>>"))
        editmenu.add_command(label="Pegar", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menubar.add_cascade(label="Editar", menu=editmenu)
        # Fuente
        fontmenu = tk.Menu(menubar, tearoff=0)
        fontmenu.add_command(label="Cambiar fuente...", command=self.cambiar_fuente)
        menubar.add_cascade(label="Fuente", menu=fontmenu)
        self.config(menu=menubar)

    def abrir_archivo(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
            self.archivo_actual = filepath
            self.title(f"Editor de Notas - {filepath}")
            self.modificado = False
            self.actualizar_numeros()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        if self.archivo_actual is None:
            return self.guardar_como()
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(self.archivo_actual, "w", encoding="utf-8") as file:
                file.write(contenido)
            self.title(f"Editor de Notas - {self.archivo_actual}")
            self.modificado = False
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    def guardar_como(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not filepath:
            return
        self.archivo_actual = filepath
        self.guardar_archivo()

    def preguntar_cerrar(self):
        if self.modificado:
            r = messagebox.askyesnocancel("Guardar cambios", "El archivo ha sido modificado.\n¿Guardar antes de salir?")
            if r is None:
                return
            elif r:
                self.guardar_archivo()
        self.destroy()

    def on_modificado(self, event=None):
        if self.text_area.edit_modified():
            self.modificado = True
            self.text_area.edit_modified(False)
            self.actualizar_numeros()

    # Numeración de líneas
    def actualizar_numeros(self):
        self.lineas.config(state="normal")
        self.lineas.delete(1.0, tk.END)
        lineas_visibles = self.text_area.index('@0,0').split('.')[0]
        total = int(self.text_area.index(tk.END).split('.')[0])
        numeros = "\n".join(str(i) for i in range(1, total)) + "\n"
        self.lineas.insert(1.0, numeros)
        self.lineas.config(state="disabled")

    # Sincronizar scroll de margen/área
    def scroll_todo(self, *args):
        self.text_area.yview(*args)
        self.lineas.yview(*args)
    def on_scroll(self,*args):
        self.scroll.set(*args)
        self.lineas.yview_moveto(args[0])

    def cambiar_fuente(self):
        familia = simpledialog.askstring("Fuente", "Familia de fuente:", initialvalue=self.fuente_actual.actual('family'))
        if not familia:
            return
        try:
            size = int(simpledialog.askinteger("Fuente", "Tamaño de fuente:", initialvalue=self.fuente_actual.actual('size')))
        except:
            size = self.fuente_actual.actual('size')
        try:
            nueva_fuente = font.Font(family=familia, size=size)
            self.fuente_actual = nueva_fuente
            self.text_area.configure(font=nueva_fuente)
            self.lineas.configure(font=nueva_fuente)
        except Exception as e:
            messagebox.showerror("Error de fuente", f"No se pudo cambiar la fuente:\n{e}")

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
