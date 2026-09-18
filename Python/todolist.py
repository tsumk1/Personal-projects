#!/usr/bin/env python3

#To-do list 
import tkinter as tk
import json
from tkinter import PhotoImage
from PIL import Image, ImageTk

FILENAME = "task.json"


def load_tasks():
    try:
        with open("task.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("task.json", "w") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(tasks, task):
    tasks.append({"text": task, "done": False})

def remove_task(tasks, index):
    tasks.pop(index)

def remove_all():
    tasks.clear()
    save_tasks(tasks)
    refresh_listbox()

def toggle_done(tasks, index):
    tasks[index]["done"] = not tasks[index]["done"]

tasks = load_tasks()

root = tk.Tk()
root.title("Listbox")
root.geometry("500x700")  # Розмір вікна 
root.config(bg="#ca1c1c")
root.resizable(False, False) 

icon_img = tk.PhotoImage(file="images(1).png")
root.iconphoto(True, icon_img)


img = Image.open("images(1).png")
img = img.resize((500, 700))          # ось тут реально змінюється розмір картинки
root_img = ImageTk.PhotoImage(img)     # перетворюємо в формат для tkinter

bg_label = tk.Label(root, image=root_img)
bg_label.place(x=0, y=0)




def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
       prefix = "✅ " if task["done"] else "◻️ "
       listbox.insert(tk.END, prefix + task["text"])

def on_add_click():
    text = entry.get()         
    if text != "":
        add_task(tasks, text)   
        save_tasks(tasks)       
        refresh_listbox()       
        entry.delete(0, tk.END) 

def on_delete_click():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        remove_task(tasks, index)
        save_tasks(tasks)
        refresh_listbox()

def on_task_click(event):
    index = listbox.nearest(event.y)
    toggle_done(tasks, index)
    save_tasks(tasks)
    refresh_listbox()

entry_label = tk.Label(root, text="Напиши сюди нову задачу", bg = "pink")
entry_label.pack(pady=10, padx=5)


entry = tk.Entry(root)
entry.pack(pady=10, padx=5) # тут тоже відступи 

add_button = tk.Button(root, text="Додати", command=on_add_click, bg="#472D79", fg="white", width=20, height=1, activebackground="#a47fe0")
add_button.pack(pady=10, padx=5)   # відступ зверху/знизу і зліва/справа

listbox = tk.Listbox(root, bd = 4, highlightbackground="red", highlightthickness=2)
listbox.pack(pady=10, padx=5)
listbox.bind("<Button-1>", on_task_click)


delete_button = tk.Button(root, text="Видалити", command=on_delete_click, bg="#691d1d", fg="white", activebackground="#c75d5d", width=20, height=1)
delete_button.pack(pady=5, padx=5)

delete_all_button = tk.Button(root, text="Очистити список", command=remove_all , bg="#691d1d", fg="white", activebackground="#c75d5d", width=20, height=1)
delete_all_button.pack(pady=5, padx=5)
refresh_listbox()

root.mainloop()