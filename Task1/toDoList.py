s_no = 1        #global var

class to_do_list:
    def __init__(self):
        self.list = {}
    
    
    def addNew(self, task):
        global s_no
        self.list[s_no] = {"Task": task}
        s_no+=1
    
    
    def viewTask(self):
        print("\nTo Do List:-")
        if not self.list:
            print("<Empty>")
            return
        
        for s_no, details in self.list.items():
            print(f"Task {s_no}: {details['Task']}")

            
    def updateTask(self, num, task):
        num = int(num)
        
        for s_no, details in self.list.items():
            if s_no == num:
                self.list[s_no]["Task"] = task
                print(f"Task {num} is updated")
                break
        
        
    def deleteTask(self, num):
        global s_no
        
        if num in self.list:
            self.list.pop(num)
            
            # Rearrange the remaining tasks
            for i in range(num, s_no - 1):
                self.list[i] = self.list.pop(i + 1)
            
            s_no -= 1
            print(f"Task {num} is deleted.")
            
        else:
            print(f"Task {num} not found.") 
        

#Main()_Body
todo = to_do_list()

while True:

    todo.viewTask()
    
    print("\n\tMAIN MENU")
    print("1. Add New Task")
    print("2. Update a Task")
    print("3. Delete a Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":
        task= input("Enter the task: ")
        todo.addNew(task)

    elif choice == "2":
        while True:
            num=int(input("Enter the task no.: "))
            if num>=s_no or num<=0 :
                print(f"Task {num} not found.\n")
            
            else:
                task=input("Enter the updated task: ")
                todo.updateTask(num, task)
                break
        
    elif choice == "3":
        while True:
            num=int(input("Enter the task no.: "))
            
            todo.deleteTask(num)
            break
    
    elif choice == "4":
        while True:
            choice2 = input("Want to Exit (Y/N): ")
            
            if choice2 == 'y' or choice2 == 'Y':
                print("\nExiting Program.")
                exit()
            elif choice2 == 'n' or choice2 == 'N':
                break
            else:
                print("Invalid choice. Please select a valid option.")
        
    else:
        print("Invalid choice. Please select a valid option.")
    