#!/usr/bin/env python 3
from tkinter import * 
import tkinter as ttk
import webbrowser

def main():
    window = ttk.Tk()
    window.geometry("300x200")
    window.configure(bg = "grey")

    # Pravimo unos
    unos = ttk.Entry(window)
    unos.pack()
    unos.get()

    def callback():
        unos_link = unos.get()
        link1 = ttk.Label(window, text = unos_link, fg = "black", cursor = "plus")
        link1.bind("<Button-1>", lambda event: webbrowser.open_new(link1.cget("text")))
        link1.pack()

    # Dugme koje dodaje link
    dodaj = ttk.Button(window, text = "Add Link", bg = "blue", fg = "black", command = callback)
    dodaj.pack()

    window.mainloop()

if __name__ == "__main__":
    main()