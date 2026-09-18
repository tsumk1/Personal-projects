#Create an empty list and a function add_task(tasks, task), which adds a new item to the list.
def add_task(tasks, task):
    """Додає нову задачу в список tasks"""
    tasks.append(task)


# --- Перевірка роботи функції ---

tasks = []  # створюємо порожній список задач

add_task(tasks, "Купити хліб")
add_task(tasks, "Зробити домашку")
add_task(tasks, "Погуляти з собакою")

print(tasks)