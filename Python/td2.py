#Write a function remove_task(tasks, index), which removes an element by number.
def remove_task(tasks, index):
    try: 
        tasks.pop(index)
    except:
        print("Такого завдання не існує")

tasks = ["Купити хліб", "Зробити домашку", "Погуляти з собакою"]
print(tasks)

remove_task(tasks, 1)
print(tasks)

remove_task(tasks, 4)
