import json

from task import Task


class TaskManager:
    def __init__(self):
        self.id_task = 0
        self.task = None
        self.task_list = []

    def _get_title_description_input(self):
        """
        solicita al usuario el titulo y la descripcion
        """
        # validacion si en dado caso entre otro tipo de formato diferente a string
        try:
            title = input("Titulo: ")
            description = input("Descripcion: ")
            if isinstance(title, str) or isinstance(description, str):
                return title, description
        except TypeError as e:
            print(f"Error de tipo: {e}")

    def add_task(self):
        print("\nAgregar tarea")
        # asignamos metodo a las variable
        title, description = self._get_title_description_input()
        self.id_task += 1

        # Guardar tarea en lista
        task = Task(self.id_task, title, description)
        self.task_list.append(task.to_dict())

    def view_task(self):
        print("\n Vista de tareas")
        
        # Iterancion de lista con los datos de la Task
        for iter in self.task_list:
            task = iter
            data = json.load(task)
            print(data)


tarea = TaskManager()
tarea.add_task()
tarea.add_task()
tarea.add_task()

tarea.view_task()
