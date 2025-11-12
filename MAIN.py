from tkinter import *

from Check_tasks import CheckTasksWindow 
from Create_task import CreateTaskWindow
from Edit_task import EditTaskWindow
from Read_tasks import read_tasks_from_file


class ToDoApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("My TO DO List") 
        self.minsize(width=500, height=500)
        self.config(padx=20, pady=20)

        self.canvas = Canvas(width=400, height=300)
        self.canvas.grid(row= 0, column= 1, rowspan= 2)
        self.logo_image = PhotoImage(file="task_manager.png")
        self.background = self.canvas.create_image(200, 150, image= self.logo_image)

        self.create_widgets()

    def create_widgets(self):
        # Create buttons to open new windows
        self.grid_columnconfigure(0, weight= 1)
        self.grid_columnconfigure(1, weight= 1)
        self.grid_columnconfigure(2, weight= 1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        add_task_button = Button(self, text="Add New Task", command=self.open_create_task_window)
        add_task_button.grid(row=0, column=0, padx=10, pady=50, sticky="nsew")

        edit_task_button = Button(self, text="Edit Existing Task", command=self.open_edit_task_window)
        edit_task_button.grid(row=1, column=0, padx=10, pady=50, sticky="nsew")

        check_tasks_button = Button(self, text= "Check Created Tasks", command= self.open_created_tasks_window)
        check_tasks_button.grid(row=2, column=0, padx=10, pady=35, sticky="nsew")
 
    def open_create_task_window(self):
        CreateTaskWindow(self)  # Pass the main app instance to the new window

    def open_edit_task_window(self):
        EditTaskWindow(self)  # Pass the main app instance to the new window

    def open_created_tasks_window(self):
        loaded_tasks = read_tasks_from_file()
        CheckTasksWindow(self, tasks_list= loaded_tasks)

# if __name__ == "__main__":
app = ToDoApp() #starts the application  
app.mainloop()

