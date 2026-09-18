#Навчись зберігати список задач у файл через json.dump()
import json 


tasks = [{"text": "Купити хліб", "done": False}, 
         {"text": "Купити молоко", "done": True}, 
         {"text": "Купити сало", "done": False}]

with open("task.json", "w") as f:
    json.dump(tasks, f, ensure_ascii=False, indent=4)

print("Задачі збережено у файл tasks.json")