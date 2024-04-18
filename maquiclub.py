import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, Label, Frame
from PIL import Image
from rembg import remove
import webbrowser

def open_file(file_types):
    filepath = filedialog.askopenfilename(
        filetypes=file_types,
        title="Seleccionar archivo"
    )
    if filepath:
        return filepath
    else:
        messagebox.showinfo("Info", "No se seleccionó ningún archivo.")
        return None

def save_file(file_type):
    filepath = filedialog.asksaveasfilename(
        defaultextension=file_type,
        filetypes=[(f"{file_type.upper()} files", f"*{file_type}")],
        title=f"Guardar como {file_type.upper()}"
    )
    if filepath:
        return filepath
    else:
        messagebox.showinfo("Info", "No se seleccionó ningún archivo.")
        return None

def convert_to_png():
    input_path = open_file([("WebP files", "*.webp")])
    if input_path:
        output_path = save_file(".png")
        if output_path:
            try:
                with Image.open(input_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(output_path, 'PNG')
                    messagebox.showinfo("Éxito", "Imagen convertida a PNG exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Un error ocurrió: {e}")

def remove_background():
    input_path = open_file([("Image files", "*.png;*.jpg;*.jpeg;*.webp")])
    if input_path:
        output_path = save_file(".png")
        if output_path:
            try:
                with Image.open(input_path) as img:
                    img = remove(img)
                    img.save(output_path, 'PNG')
                    messagebox.showinfo("Éxito", "Fondo removido y imagen guardada exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Un error ocurrió: {e}")

def open_link(url):
    webbrowser.open_new(url)

root = tk.Tk()
root.title("Maquiclub v1")
root.geometry("300x200")  

frame = Frame(root)
frame.pack(pady=20)

label = Label(frame, text="Seleccione la operación que desea realizar:")
label.pack(pady=10)

convert_button = tk.Button(frame, text="Convertir WebP a PNG", command=convert_to_png)
convert_button.pack(pady=5)

remove_bg_button = tk.Button(frame, text="Eliminar fondo de una imagen", command=remove_background)
remove_bg_button.pack(pady=5)

signature_label = Label(frame, text="Hecho con ❤ por Para", fg="gray", cursor="hand2")
signature_label.pack(pady=10)
signature_label.bind("<Button-1>", lambda e: open_link("https://eliecer.bio"))

root.mainloop()
