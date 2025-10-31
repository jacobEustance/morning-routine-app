tasks = []

def addtask():
    task = input("pls enter task: ")
    tasks.append(task)
    print(f'Task "{task}" has been added to the list')

def deltask():
    listtasks()
    
    try:
        tasktodelete = int(input("choose the number of task to delete: "))
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print('Task removed!')
        
        else:
            print(f'Task #{tasktodelete} was not found')
    
    
    except:
        print('invalid input')
def listtasks():
    if not tasks:
        print('there are no tasks currently')
    else:
        print("current tasks: ")
        for index, task in enumerate(tasks):
            print(f'Task #{index}. {task}')



if __name__ == "__main__":
# Create a loop to run app
    print("These are you tasks for the morning: ")
    while True: 
        print('\n')
        print("what would you like to do? ")
        print("------------------------------")
        print('1. Add new task ')
        print('2. Delete tasks ')
        print('3. list tasks ')
        print('4. Quit')
        choice = input('enter you choice: ')

        if (choice == "1"):
            addtask()

        elif (choice == "2"):
            deltask()

        elif (choice == "3"):
            listtasks()

        elif (choice == "4"):
            break

        else:
            print('invalid input')

    print("goodbye")