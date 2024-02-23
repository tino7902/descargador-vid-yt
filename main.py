from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class ventana:
    def __init__(self, root):
        self.dir = ""

        self.root = root
        self.root.title("descargador de videos")

        self.url_label = tk.Label(root, text="Ingresar el url del video ", font=("Helvetica", 18))
        self.url_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.dir_label = tk.Label(root, text="Donde desea guardar la descarga? ", font=("Helvetica", 18))
        self.dir_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.url_entry = tk.Entry(root, font=("Helvetica", 18))
        self.url_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.dir_boton = tk.Button(root, text="Elegir carpeta", font=("Helvetica", 18), command=self.file_dialog)
        self.dir_boton.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.iniciar = tk.Button(root, text="Listo", command=lambda: self.descargar_video(self.dir), font=("Helvetica", 18))
        self.iniciar.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)


    def descargar_video(self, dir_guardado):
        try:
            url = self.url_entry.get()

            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            mayor_res = streams.get_highest_resolution()
            mayor_res.download(output_path=dir_guardado)
            print(f"video descargado en la mayor resolución disponible\nGuardado en {dir_guardado}")
            messagebox.showinfo(title="List !", message="Descarga completada !")

        except Exception as e:
            print(e)

    def file_dialog(self):
        dir = filedialog.askdirectory()
        if dir:
            print(f"carpeta elegida: {dir}")
            self.dir = dir
            self.dir_label.config(text=f"carpeta elegida: {self.dir}")
            self.dir_boton.config(text="Cambiar")


if __name__ == "__main__":
    root = tk.Tk()
    app = ventana(root)
    root.mainloop()