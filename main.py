from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def descargar_video(url, dir_guardado):
    try:
        yt = YouTube(url)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    pass