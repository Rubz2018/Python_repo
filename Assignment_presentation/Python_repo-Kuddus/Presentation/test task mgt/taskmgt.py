# This script implements a simple command-line Todo List application.
# It allows users to add, list, mark as complete, and remove tasks.
# Each task has a description and a completion status.
# The application runs in a loop until the user chooses to exit.
# // The tasks are stored in memory and not persisted to a file.
# The user can interact with the application through a simple text-based menu.
# The script is designed to be run in a terminal or command prompt.

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
    
    def mark_complete(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nYour Todo List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
    
    def mark_task_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number!")
    
    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task number!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            todo_list.list_tasks()
            task_num = int(input("Enter task number to mark complete: "))
            todo_list.mark_task_complete(task_num)
        elif choice == "4":
            todo_list.list_tasks()
            task_num = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()