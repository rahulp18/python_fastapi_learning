
import json
class Task:
    def __init__(self,id:int,title: str,status:str):
        self.id=id
        self.title=title
        self.status=status
    def __str__(self):
        return f"{self.id} {self.title} {self.status}"
    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "status":self.status
        }

class TaskManager:
    def __init__(self,tasks:list[Task]):
        self.tasks=tasks
        self.load_tasks()
    
    def get_tasks(self):
        return self.tasks
    def add_task(self,task:Task):
        self.tasks.append(task)
        self.save_tasks()
    def delete_task(self,id:int):
        for index,task in enumerate(self.tasks):
            if task.id==id:
                self.tasks.pop(index)
                break
        self.save_tasks()

    def update_task(self,id:int,status:str):
        for index,task in enumerate(self.tasks):
            if id==task.id:
                 task.status=status
        self.save_tasks()
                
    def get_task_by_id(self,id:int):
        for index,task in enumerate(self.tasks):
            if task.id==id:
                return task
        return None
    def save_tasks(self):
        tasks_data=[]
        for task in self.tasks:
            tasks_data.append(task.to_dict())
         
        with open("tasks.json","w") as file:
            json.dump(tasks_data, file, indent=4)
    def load_tasks(self):
        try:
            with open("tasks.json",'r') as file:
                tasks_data=json.load(file)

                for task in tasks_data:
                    new_task=Task(task['id'],task["title"],task["status"])

                    self.tasks.append(new_task)
        except FileNotFoundError:
            print("No tasks file exists")


    
def execute(taskManager:TaskManager):
  
    while True:
        print("Hello, Please pick one option to proceed...\n")
        print("1:Create Task(1)\n")
        print("2:Get all Tasks(2)\n")
        print("3:Get Task By Id (3)\n")
        print("4:Update Task (4)\n")
        print("5:Delete Task (5)\n")
        print("If want to exit press 6 \n")

        choice=input("Enter your choice Number \n")
        run_tasks(choice,taskManager)
        ch=input("Want to continue ? yes/no \n")

        if choice=="6" or ch=="no":
            break

def run_tasks(choice:str,taskManager:TaskManager):
    match choice:
        case "1":
          userInput=input('Enter your tak in the bellow format\n 1-Create Schema-pending\n')
          splitArr=userInput.split("-")
          
          if len(splitArr)!=3:
              print("Invalid Task Format\n")
              return
          task=Task(int(splitArr[0]),splitArr[1],splitArr[2])
          taskManager.add_task(task)
          print("Your Task has been added\n")
        case "2":
            tasks=taskManager.get_tasks()
            if(len(tasks)==0):
                print("No tasks are available")
            for task in tasks:
                 print(task)
        case "3":
            userInput=int(input("Enter Task Id\n"))
            task=taskManager.get_task_by_id(userInput)
            print(f"{task.id}  {task.title} {task.status}")
        case "4":
            taskId=int(input("Enter task id\n"))
            status=input("Enter task status\n")
            taskManager.update_task(taskId,status)
            print("Task Updated\n")
        case "5":
            taskId=int(input("Enter task id\n"))
            taskManager.delete_task(taskId)
            print("Task deleted!\n")
        case "6":
            print("Thank You!")
taskManager=TaskManager([])           
execute(taskManager)


           


