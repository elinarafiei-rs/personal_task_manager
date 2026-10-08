from tasks import add_tasks

name = input("Enter your name: ")
print(f"Welcome", name)

tasks = []
while True:
    task = input("please enter ypur task(if you don't want to enter any task(done)) :")

    if task.lower() == "done":
        break
    tasks.append(task)

print("Enter a task: ")
for task in tasks:
    print("-", task)