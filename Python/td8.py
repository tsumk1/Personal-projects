#9. Створи просте вікно tkinter з заголовком і кнопкою, яка виводить повідомлення в консоль при натисканні (Button, command).
import tkinter as tk 
def say_hello():
    print("Knopka rabotait")
root = tk.Tk()
root.title("Miй перший додаток")
def show_text():
    text = entry.get()          # беремо те, що ввів користувач
    label.config(text=text)     # виводимо це в Label


button = tk.Button(root, text="Knopka", command=say_hello)
button.pack()

entry = tk.Entry(root)
entry.pack()


label = tk.Label(root, text="Тут буде текст")
label.pack()


button2 = tk.Button(root, text="Pokakat", command=show_text)
button2.pack()
root.mainloop()