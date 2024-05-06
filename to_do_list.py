def display(to_list):
    print("TO-DO List:")
    for index,task in enumerate(to_list):
        print(f"{index+1}.{task}")
def add_list(todo_list,task):
    todo_list.append(task)
    print(f"Task {task} added to the to-do list")
def remove_list(todo_list,index):
    if index>=0 and index<len(todo_list):
        remove_task=todo_list.pop(index)
        print(f"Task {remove_task} removed from the to-do list")
    else:
        print("Invalid index")
def main():
    to_list=[]
    while True:
        print("\n1.Display TO-DO LIST")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Exit")

        choice=int(input("Enter your Choice:"))
        if choice==1:
            display(to_list)

        elif choice==2:
            task=input("Enter the Task to add:")
            add_list(to_list,task)
        elif choice==3:
            index=int(input("Enter index of task tp remove:"))-1
            remove_list(to_list,index)
        elif choice==4:
            print("Exiting program.")
            break
        else:
            print("Invaild choice.Please try again.")


if __name__=="__main__":
    main()
