from tkinter import Toplevel, Label, N, W, E


class CheckTasksWindow(Toplevel):
    def __init__(self, parent, tasks_list):
        super().__init__(parent)
        self.parent = parent
        self.title("Check Created Tasks")
        self.minsize(width=400, height=300)
        self.tasks = tasks_list
        self.grab_set()
        self.transient(parent)
        self.display_tasks() 

    def display_tasks(self):
        name = Label(self, text= "Current Task List", font= ("Arial", 12, "bold"))
        name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky= W)

        for i, task in enumerate(self.tasks):
            Label(self, text= f"{i+1}").grid(row= i+1, column=0, padx=10, sticky= N+W)
            Label(self, text= task, anchor= W).grid(row= i+1, column= 1, padx= 5, pady= 2, sticky= N+W+E)

        self.grid_columnconfigure(1, weight= 1)