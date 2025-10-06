# tk_intro.py
import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title("Python UI")
main_window.geometry("600x400")

def on_click():
    messagebox.showinfo("Information", "You clicked the button")

button = tk.Button(main_window, text="Press Me", command=on_click)
button.place(x=10, y=20)

main_window.mainloop()