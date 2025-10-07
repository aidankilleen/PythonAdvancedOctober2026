# tk_intro.py
import tkinter as tk
from tkinter import messagebox

from UserDAO import UserDAO

import threading, time, queue



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


q = queue.Queue()

def long_task():
    time.sleep(3)           # simulate blocking I/O / CPU
    q.put("Done!")          # send result back

def on_slow_click():
    btn.config(state="disabled", text="Working…")
    threading.Thread(target=long_task, daemon=True).start()
    main_window.after(100, poll_queue)

def poll_queue():
    try:
        msg = q.get_nowait()
    except queue.Empty:
        main_window.after(100, poll_queue)
        return
    btn.config(state="normal", text=msg)

btn = tk.Button(main_window, text="Do work", command=on_slow_click)
btn.place(x=10, y=100)

main_window.mainloop()