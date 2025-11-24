class Task:
    idTask = 0

    def __init__(self, title, body, status=False):
        Task.idTask += 1  # increment the class counter
        self.id = Task.idTask
        self.title = title
        self.body = body
        self.status = status

    # return dict
    def __str__(self):
        return (
            f"id: {self.id}\n"
            f"title: {self.title}\n"
            f"body: {self.body}\n"
            f"status: {self.status}\n"
            f"-----------------------"
        )


class TaskMager:
    def __init__(self):
        self.listDict = []

    def addTask(self):
        titleTask = input("Title: ")
        descTask = input("Task: ")

        task = Task(titleTask, descTask)  # Transfer date to class Task
        self.listDict.append(task)  # Transfer dictionary to listDict

        print("Task Add.!")
        print("---------")
        print("1) Add Task.")
        print("2) Return.")

        self.running = True
        while self.running:
            opt = input("Selections a optionst: ")
            if opt == "1":
                return self.addTask()
            elif opt == "2":
                return
            else:
                print("Invalid option.")

    def listTask(self):
        print(self.listDict)
        for task in self.listDict:
            print(task)

    def exit_program(self):
        self.running = False

    def menu(self):
        menuOpt = {
            "1": self.addTask,
            "2": self.listTask,
            # "3": self.status,
            # "4": self.remove,
            "5": self.exit_program,
        }

        self.running = True
        while self.running:
            # Imprimimos las opciones
            print("TASK MANAGER")
            print("1) Add task")
            print("2) List task")
            print("3) Complete task")
            print("4) Remove task")
            print("5) Exit")
            print("----------------------------------")

            opt = input("Selection a options: ")

            if opt in menuOpt:
                menuOpt[opt]()
            else:
                print("Invalid options.")


if __name__ == "__main__":
    task = TaskMager()
    task.menu()
    # task.listTask()
