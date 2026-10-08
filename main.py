from tasks import add_tasks

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