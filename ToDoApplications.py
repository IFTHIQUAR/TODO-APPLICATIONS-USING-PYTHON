import pandas as pd
def todo():
    task=[]
    total_task=int(input("Enter Total No of Task: "))
    for tasks in range(0,total_task):
        task_name=input("Enter task name:")
        task.append(task_name)
    df=pd.DataFrame(task,columns=['Task Name'])
    df.index+=1
    print(df)
    while True:
        print("LIST OF TODO OPERATIONS")
        print("\n1.Add task\n2.Update Task\n3.Delete Task\n4.Display Task\n5.Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            new_task=input("Enter your New task: ")
            if new_task in task:
                print(f"The Task {new_task} is already Exists!!!... please Enter Other Task")
            else:
                task.append(new_task)
                print(f"The Task {new_task} Added Successfully")
        elif choice==2:
            old_task=input("Enter your old task to update: ")
            if old_task not in task:
                print(f"The Task {old_task} is NOT EXITS in the current task list!!!...")
            else:
                new_task=input("Enter your New task to Update with old task: ")
                old_task_index=task.index(old_task)
                task[old_task_index]=new_task
                print(f"The New Task {new_task} Added Successfully")
        elif choice==3:
            del_task=input("Enter your task to delete:")
            if del_task not in task:
                print(f"The task {del_task} not available in the current task")
            else:
                task.remove(del_task)
                print(f"The task {del_task} is removed Successfully")
        elif choice==4:
            df=pd.DataFrame(task,columns=['Task Name'])
            df.index+=1
            print(df)
        elif choice==5:
            print("TOD APP CLOSED SUCCESSFULLY")
            break
        else:
            print("YOU HAVE SELECTED WRONG CHOICE ")
todo()