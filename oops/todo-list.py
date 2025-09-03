
class TodoList:
    def __init__(self) -> None:
        self.__tasks = []
    
    def add_task(self,title):
        task = {"id":len(self.__tasks) + 1,
                "title":title,
                "completed":False
                }
        self.__tasks.append(task)
        
    def remove_task(self,id:int):
        self.__tasks = list(filter(lambda task:task['id'] != id, self.__tasks))
    
    def mark_as_completed(self, id: int):
        self.__tasks = [
            {**task, "completed": True} if task["id"] == id else task
            for task in self.__tasks
        ]
        # or
        # self.__tasks = list(
        #     map(
        #         lambda task: {**task, "completed": True} if task["id"] == id else task,
        #         self.__tasks
        #     ))
    def get_all_task(self):
        return self.__tasks
    
    def get_uncompleted_tasks(self):
        # return list(filter(lambda task: not task['completed'], self.__tasks))
        return [task for task in self.__tasks if not task['completed']]
    
    def get_completed_task(self):
        # return list(filter(lambda task: task['completed'], self.__tasks))
        return [task for task in self.__tasks if task['completed']]
    
    def search_task(self,title:str):
        # return list(filter(lambda task: task['title'].lower() == title.lower(), self.__tasks))
        return [task for task in self.__tasks if task['title'].lower() == title.lower()]
    
    def sort_tasks(self):
        self.__tasks = sorted(self.__tasks,key=lambda task:task['title'].lower())


class TodoCLI:
    def __init__(self,todo_list:TodoList,) -> None:
        self.__todo_list = todo_list
    
    def display_task_list(self,task_list:list[dict],empty_message="No tasks found"):
        if not task_list:
            print(empty_message)
        for task in task_list:
            print(f"{{id: { task['id']},title: {task['title']},completed: {task['completed']}}}")   
        
    def display_menu(self):
        print("""***** WELCOME TO TODO LIST SYSTEM ****
1. Add Task
2. Remove Task
3. Mark Task as Completed
4. Display All Tasks
5. Display Uncompleted Tasks
6. Display Completed Tasks
7. Search Task
8. Sort Tasks
9. Exit
""")
    def run(self):
        self.display_menu()
        while True:
            option = input("Option: ")
            match option:
                case '1':
                    title = input("Title: ")
                    self.__todo_list.add_task(title)
                case '2':
                    id = int(input("Id: "))
                    self.__todo_list.remove_task(id)
                case '3':
                    id = int(input("Id: "))
                    self.__todo_list.mark_as_completed(id)
                case '4':
                    self.display_task_list(self.__todo_list.get_all_task())
                case '5':
                    self.display_task_list(self.__todo_list.get_uncompleted_tasks())
                case '6':
                    self.display_task_list(self.__todo_list.get_completed_task())
                case '7':
                    title = input("Title: ")
                    self.display_task_list(self.__todo_list.search_task(title))
                case '8':
                    self.__todo_list.sort_tasks()
                case '9':
                    print("Exiting...")
                    break
                case _:
                    print("Invalid Option")
                    
                    
                    
if __name__ == "__main__":                               
    todo_list = TodoList()
    cli = TodoCLI(todo_list)
    cli.run()