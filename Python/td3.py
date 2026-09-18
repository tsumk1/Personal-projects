#Write a function show_tasks(tasks) that displays all tasks with numbering (1, 2, 3...).
def show_tasks(tasks):
 for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

tasks = ["Купити хліб", "Купити молоко", "Купити сир"]

show_tasks(tasks)