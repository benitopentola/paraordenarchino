import tkinter as tk
from tkinter import scrolledtext, messagebox

def ordenar_lineas(lineas):
    lineas_ordenadas = []

    for linea in lineas:
        # Dividir la línea en sus componentes
        componentes = linea.strip().split('\t')

        # Buscar el componente que contiene el carácter chino
        for idx, componente in enumerate(componentes):
            if any('\u4e00' <= c <= '\u9fff' for c in componente):
                # Si se encuentra un carácter chino, moverlo al principio de la línea
                chino = componente
                del componentes[idx]
                lineas_ordenadas.append('\t'.join([chino] + componentes))
                break
        else:
            # Si no se encuentra ningún carácter chino en la línea, mantener el orden original
            lineas_ordenadas.append('\t'.join(componentes))

    return lineas_ordenadas

def ordenar_texto():
    texto_entrada = entrada_texto.get("1.0", "end").strip()
    lineas = texto_entrada.split('\n')
    if len(lineas) <= 1:
        messagebox.showerror("Error", "Introduce al menos dos líneas de texto.")
        return
    lineas_ordenadas = ordenar_lineas(lineas)
    texto_salida.delete("1.0", "end")
    texto_salida.insert("1.0", "\n".join(lineas_ordenadas))

def copiar_texto():
    texto = texto_salida.get("1.0", "end")
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    messagebox.showinfo("Copiado", "Texto copiado al portapapeles.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ordenador de Texto")

# Crear cuadro de texto de entrada
etiqueta_entrada = tk.Label(ventana, text="Introduce las líneas de texto (caracteres en chino, traducción al español, pinyin):")
etiqueta_entrada.pack()
entrada_texto = scrolledtext.ScrolledText(ventana, width=50, height=10)
entrada_texto.pack()

# Crear botón de ordenar
boton_ordenar = tk.Button(ventana, text="Ordenar", command=ordenar_texto)
boton_ordenar.pack()

# Crear cuadro de texto de salida
etiqueta_salida = tk.Label(ventana, text="Texto ordenado:")
etiqueta_salida.pack()
texto_salida = scrolledtext.ScrolledText(ventana, width=50, height=10)
texto_salida.pack()

# Crear botón de copiar
boton_copiar = tk.Button(ventana, text="Copiar texto", command=copiar_texto)
boton_copiar.pack()

# Ejecutar la ventana principal
ventana.mainloop()
