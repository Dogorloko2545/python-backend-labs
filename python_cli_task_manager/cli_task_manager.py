class Task:
    idTask = 0

    def __init__(self, title, body, status=False):
        Task.idTask += 1  # increment the class counter
        self.title = title
        self.body = body
        self.status = status

    # return dict
    def dictTak(self):
        return {
            "id": Task.idTask,
            "title": self.title,
            "body": self.body,
            "status": self.status,
        }


class TaskMager:
    def __init__(self):
        self.listDict = []

    def addTask(self):
        titleTask = input("Title: ")
        descTask = input("Task: ")

        task = Task(titleTask, descTask)  # Transfer date to class Task
        self.listDict.append(task.dictTak())  # Transfer dictionary to listDict

        print("Task Add.!")
        print("---------")
        print("1) Add Task.")
        print("2) Return.")

        while True:
            opt = input("Selections a optionst: ")
            if opt == "1":
                self.addTask()
            elif opt == "2":
                self.menu()
            else:
                print("Invalid option.")

    def listTask(self):
        for dictionary in self.listDict:
            # access the list of dictionary
            print(f"id: {dictionary['id']}")
            print(f"title: {dictionary['title']}")
            print(f"body: {dictionary['body']}")
            print(f"status: {dictionary['status']}")
            print("-----------------------------")

    def exit_program(self):
        """Finaliza la ejecución del programa."""
        print("\n-> Saliendo del programa. ¡Adiós!")
        exit()

    def menu(self):
        menuOpt = {
            "1": self.addTask,
            "2": self.listTask,
            # "3": self.status,
            # "4": self.remove,
            "5": self.exit_program,
        }

        while True:
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
