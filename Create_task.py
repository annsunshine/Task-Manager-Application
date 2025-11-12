from tkinter import *
from tkinter import messagebox, Toplevel
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

class CreateTaskWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Create New Task")
        self.minsize(width=400, height=300)

        self.PRIORITY = ["High", "Medium", "Low"]
        self.STATUS = ["Not started", "In progress", "Completed"]


        self.ID_entry = Entry(self, width= 21)
        self.ID_entry.grid(column=1, row=1, columnspan=2)
        self.name_of_the_task_entry = Entry(self, width= 21)
        self.name_of_the_task_entry.grid(column=1, row=2, columnspan=2)
        self.deadline_entry = DateEntry(self, selectmode= 'day',date_pattern= 'yyyy-mm-dd', width= 20)
        self.deadline_entry.grid(column=1, row=3, columnspan= 2) 
        self.deadline_entry.delete(0, END)
        self.priority_combobox = Combobox(self, values= self.PRIORITY, state= "readonly")
        self.priority_combobox.grid(column=1, row=4, columnspan=2)
        self.priority_combobox.set("Select Priority")
        self.status_combobox = Combobox(self, values= self.STATUS, state= "readonly")
        self.status_combobox.grid(column=1, row=5, columnspan=2)
        self.status_combobox.set("Select Status")

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

        save_button = Button(self, text="Save Task", command= self.save_task)
        save_button.grid(row=6, column=4)


    def save_task(self):

        task_id = self.ID_entry.get()
        task_name = self.name_of_the_task_entry.get()
        task_deadline = self.deadline_entry.get()
        task_priority = self.priority_combobox.get()
        task_status = self.status_combobox.get()

        PRIORITY_PLACEHOLDER = "Select Priority"
        STATUS_PLACEHOLDER = "Select Status"

        if not task_id or not task_name or not task_deadline or not task_priority or not task_status or task_priority == PRIORITY_PLACEHOLDER or task_status == STATUS_PLACEHOLDER:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        else:
            try:
                with open("data.txt", "a") as file:
                    file.write(f"{task_id} | {task_name} | {task_deadline} | {task_priority} | {task_status}\n")
                messagebox.showinfo("Success", "Task created successfully!")
            except Exception as e:
                messagebox.showerror(title="Error", message=f"An unexpected error occurred: {e}")
        self.destroy()



