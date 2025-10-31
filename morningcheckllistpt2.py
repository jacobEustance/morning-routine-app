tasks = ['Electrolytes', 'breakfast', 'gym', 'coffee']

def deltask():
    
    try:
        tasktodelete = int(input("choose the number of task completed: ") + 1)
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print('Task Done!')
        
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
            print(f'Task #{index + 1}. {task}')

listtasks()

if __name__ == "__main__":
# Create a loop to run app
    print("These are you tasks for the morning: ")
    while True: 
        print('\n')
        print("what would you like to do? ")
        print("------------------------------")
        
        print('1. Mark task as completed ')
        print('2. Quit')
        choice = input('enter you choice: ')

        

        if (choice == "1"):
            deltask()
            print('\n')
            listtasks()

        elif (choice == "2"):
            break

        else:
            print('invalid input')

    print("Have a good day!!")