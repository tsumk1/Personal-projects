#Створи Listbox і навчись додавати в нього елемен ти через .insert() та видаляти через .delete()
import tkinter as tk

def add_item():
    text = entry.get()
    if text != "":
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def delete_first():
    listbox.delete(0)

def selection_delete():
    selected = listbox.curselection()
    if selected:             
        index = selected[0]     
        listbox.delete(index)   



root = tk.Tk()
root.title("Listbox")

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Додати", command=add_item)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(tk.END, "Купити хліб")
listbox.insert(tk.END, "Купити мало")
listbox.insert(tk.END, "Купити сир")

delete_button = tk.Button(root, text="Видалити", command=delete_first)
delete_button.pack()

del_sel_button = tk.Button(root, text="Видалити вибране", command=selection_delete)
del_sel_button.pack()

root.mainloop()