from Task import TaskFunctions 
import db
import sys

def main():
    task = TaskFunctions()

    argv_len = len(sys.argv)
    if argv_len > 1:
        match sys.argv[1]:
            case "list":
                print(task.getAllTasks())
            case "delete":
                print(task.deleteTask(sys.argv[2]))
            case "stop":
                print(task.stopTask(sys.argv[2]))
            case "create":
                print(task.createTask(sys.argv[2]))
            case "killall":
                print(task.killAllTasks())
            case "live":
                print(task.filterTasks())
            case "update":
                if(argv_len > 3):
                    print(task.updateTask(sys.argv[2],sys.argv[3]))
                else:
                    print("message parameter missing")
            case _:
                print("your input is not recognised")
    else:
        print(
        """ 
        Please insert one of the following commands 
        -list => shows all entries 
        -delete => deletes an entry by Id 
        -stop => set the task status to false 
        -create => creates a new task 
        -update => updates the task message attribute
        """
        )
    
    db.session.close() 

if __name__ == '__main__':
    main()
