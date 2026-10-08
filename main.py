from tasks import add_tasks
from dotenv import load_dotenv
import os

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

name = input("Enter your name: ")
print(f"Welcome", name)

tasks = []
while True:
    task = add_tasks()
    tasks.append(task)
    if task.lower() == "done":
        break


print("Enter a task: ")
for task in tasks:
    print("-", task)

with open("tasks.txt", "w") as file:
    file.write("\n".join(tasks))