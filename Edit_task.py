from tkinter import *
from tkinter import messagebox, Toplevel
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

class EditTaskWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Edit Task") 
        self.minsize(width=400, height=300)

        self.PRIORITY = ["High", "Medium", "Low"]
        self.STATUS = ["Not started", "In progress", "Completed"]

        # Widgets for editing a task

        self.edit_ID_entry = Entry(self)
        self.edit_ID_entry.grid(column=1, row=1, columnspan=2)
        self.edit_name_of_the_task_entry = Entry(self)
        self.edit_name_of_the_task_entry.grid(column= 1, row= 2, columnspan= 2)
        self.edit_deadline_entry = DateEntry(self, selectmode= 'day',date_pattern= 'yyyy-mm-dd', width= 20)
        self.edit_deadline_entry.grid(column= 1, row= 3, columnspan= 2)
        self.edit_deadline_entry.delete(0, END)
        self.edit_priority_combobox = Combobox(self, values= self.PRIORITY, state= "readonly")
        self.edit_priority_combobox.grid(column= 1, row= 4, columnspan= 2)
        self.edit_priority_combobox.set("Select Priority")
        self.edit_status_combobox = Combobox(self, values= self.STATUS, state= "readonly")
        self.edit_status_combobox.grid(column= 1, row= 5, columnspan= 2)
        self.edit_status_combobox.set("Select Status")

        self.ID_label = Label(self, text="Task's number")
        self.ID_label.grid(column=0, row=1)
        self.name_of_the_task_label = Label(self, text="Task's name")
        self.name_of_the_task_label.grid(column=0, row=2)
        self.deadline_label = Label(self, text="Task's deadline")
        self.deadline_label.grid(column=0, row=3)
        self.priority_label = Label(self, text="Task's priority")
        self.priority_label.grid(column=0, row=4)
        self.status_label = Label(self, text="Task's status")
        self.status_label.grid(column=0, row=5)

        edit_button = Button(self, text="Update Task", command= self.update_task)
        edit_button.grid(row=6, column=4)

    def update_task(self):
        new_task_id = self.edit_ID_entry.get()
        new_task_name = self.edit_name_of_the_task_entry.get()
        new_task_deadline = self.edit_deadline_entry.get()
        new_task_priority = self.edit_priority_combobox.get()
        new_task_status = self.edit_status_combobox.get()

        if not new_task_id or not new_task_name or not new_task_deadline or not new_task_priority or not new_task_status:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        else:
            try:
                 with open("data.txt", "r") as data_file:
                     tasks = data_file.readlines()
            except FileNotFoundError:
                 messagebox.showerror(title= "Error", message= "No task found.")
                 return

            updated_tasks = []

            for task in tasks:
                if task[0] == new_task_id:
                    updated_task = f"{new_task_id} | {new_task_name} | {new_task_deadline} | {new_task_priority} | {new_task_status}\n"
                    updated_tasks.append(updated_task)
                else:
                    updated_tasks.append(task)

            if not tasks:
                messagebox.showinfo(title= "Not found", message= f"Task with ID {new_task_id} wasn't found.")
            else:
                try:
                    with open("data.txt", "w") as data_file:
                        data_file.writelines(updated_tasks)
                    messagebox.showinfo(title= "Success", message= "Task was updated successfully")
                except Exception as e:
                    messagebox.showerror(title= "Error", message= f"An unexpected error occurred: {e}")

        self.destroy()

