class Task:
    def __init__(self, id, title, body, status=False):
        self.id = id
        self.title = title
        self.body = body
        self.status = status

    def task_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "status": self.status,
        }


class TaskMager:
    def __init__(self):
        self.listDict = []
        self.menuOpt = ["add task", "list task", "complete task", "clear task"]

    def optMenu(self):
        menu = {
            "1": self.addTask,
            "2": self.listTask,
            "3": self.completeTask,
            "4": self.clearTask,
        }
        return menu

    def addTask(self):
        print("opt: addTask")

    def listTask(self):
        print("listTask")

    def completeTask(self):
        print("completeTask")

    def clearTask(self):
        print("clearTask")

    def run(self):

        print("----- Menu -----")
        for i, opt in enumerate(self.menuOpt, 1):
            print(f"{i}. {opt}")

        while True:        
            options = input("choose one of the options: ")

            if options in self.optMenu():
                self.optMenu()[options]()
            else:
                print("Invalid option")

if __name__ == "__main__":
    app = TaskMager()
    app.run()
