tasks= []
def add_task(tasks):
    task = input("Enter your task:").lower().strip()
    if task == "":
        print("Enter valid task!")
    if task in tasks:
        print("Task already exist!")
    else:
        tasks.append(task)
        
    with open("task.txt","a") as f:
        (f.write(task + "\n"))
          
def task_completed(tasks):
    task_complete = input("Enter completed task:").lower()
    if task_complete in tasks:
        tasks.remove(task_complete)
        print(f"{task_complete} done!")
    print("Remaining task:",tasks)
    
    with open("task.txt","w") as f:
        for i in tasks:
            f.write(i + "\n")
    
def view_task(tasks):
    with open("task.txt","r") as f:
        data = f.read()
        print(data)

def exit(tasks):
    print("Exiting program!")

while True:
    menu = {
        "1" : add_task,
        "2" : task_completed,
        "3" : view_task,
        "4" : exit
    }
    print("1.add task","2.complete task","3.view task","4.exit task")

    choice = input("Enter option:")
    if choice in menu:
        menu[choice](tasks)
        if choice == "4":
            break
    
           







    


