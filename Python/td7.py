#8. Навчись зчитувати задачі з файлу через json.load() при старті програми.
import json


def load_tasks():
    try:
        with open("task.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("task.json", "w") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


# --- Перевірка роботи ---

tasks = load_tasks()
print("Завантажені задачі:", tasks)