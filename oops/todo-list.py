
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
    
    def mark_as_completed(self,id:int):
        completed_task = [{**task,"completed":True} for task in self.__tasks if task['id'] == id]
        self.remove_task(id)
        self.__tasks = [*self.__tasks,*completed_task]

    def display_tasks(self):
        for task in self.__tasks:
            print(f"{{id: { task['id']},title: {task['title']},completed: {task['completed']}}}")
    
    def display_uncompleted_tasks(self):
        for task in self.__tasks:
            if not task['completed']:
                print(f"{{id: { task['id']},title: {task['title']},completed: {task['completed']}}}")
    
    def display_completed_tasks(self):
        for task in self.__tasks:
            if task['completed']:
                print(f"{{id: { task['id']},title: {task['title']},completed: {task['completed']}}}")
    
    def search_task(self,title:str):
        task = list(filter(lambda task:task['title'].lower() == title.lower(), self.__tasks))
        return task
    
    def display_menu(self):
        ...

todo_list = TodoList()
todo_list.add_task("new task")
todo_list.add_task("another task")

todo_list.display_tasks()

# todo_list.remove_task(2)

todo_list.mark_as_completed(1)
print("After completed")
todo_list.display_tasks()

print("completed")
todo_list.display_completed_tasks()

print("Uncompleted Task")
todo_list.display_uncompleted_tasks()

# print("Searching...")
# task = todo_list.search_task("Another task")


# print(task)