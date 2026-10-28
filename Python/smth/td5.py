#Зроби простий консольний цикл while True, який запитує команду: додати / видалити / показати / вийти.
def add_task(tasks, task):
    """Додає нову задачу в список tasks"""
    tasks.append(task)

def remove_task(tasks, index):
    try: 
        tasks.pop(index)
    except:
        print("Такого завдання не існує")

def show_tasks(tasks):
 for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

def toggle_done(tasks, index):
    tasks[index]["done"] = not tasks[index]["done"]
   
tasks = []
while True: 

 print('--------Обрати дію--------')
 print("додати")
 print("видалити")
 print("показати")
 print("вийти")

 command = input("Введіть команду: ")

 if command == "додати":
        task = input("Введи текст задачі: ")
        add_task(tasks, task)
 elif command == "видалити":
        index = int(input("Введи номер задачі для видалення: "))
        remove_task(tasks, index-1)
 elif command == "показати":
        show_tasks(tasks)
 elif command == "вийти":
     break
 else:
     print("Такої дії не існує")


