#Add the ability to mark a task as "done" — for example, store a list of dictionaries instead of strings {"text": "...", "done": False}.
def toggle_done(tasks, index):
    tasks[index]["done"] = not tasks[index]["done"]
   

tasks = [{"text": "Купити хліб", "done": False}, 
         {"text": "Купити хліб", "done": True}, 
         {"text": "Купити хліб", "done": False}]


print("До:", tasks)

toggle_done(tasks, 0)


print("Після:", tasks)