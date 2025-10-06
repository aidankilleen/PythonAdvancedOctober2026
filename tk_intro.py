# tk_intro.py
import tkinter as tk
from tkinter import messagebox

from UserDAO import UserDAO

dao = UserDAO()

users = dao.get_all()

print (users)

main_window = tk.Tk()
main_window.title("Python UI")
main_window.geometry("600x400")

def on_click():
    messagebox.showinfo("Information", "You clicked the button")

button = tk.Button(main_window, text="Press Me", command=on_click)
button.place(x=10, y=20)

lb_users = tk.Listbox(main_window, height=10)
lb_users.place(x=10, y=60)

for user in users:
    lb_users.insert(tk.END, user.name)



main_window.mainloop()