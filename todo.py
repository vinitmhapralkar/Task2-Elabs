class TodoManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file into the tasks list"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            # If file doesn't exist, start with empty list
            self.tasks = []
    
    def save_tasks(self):
        """Save current tasks list to file"""
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
    
    def add_task(self, task):
        """Add a new task to the list"""
        if task.strip():  # Only add non-empty tasks
            self.tasks.append(task.strip())
            self.save_tasks()
            print(f"✓ Added task: '{task}'")
        else:
            print("Error: Task cannot be empty!")
    
    def remove_task(self, index):
        """Remove a task by index (1-based)"""
        try:
            # Convert to 0-based index
            task_index = index - 1
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                self.save_tasks()
                print(f"✓ Removed task: '{removed_task}'")
            else:
                print(f"Error: Task number {index} doesn't exist!")
        except (ValueError, IndexError):
            print("Error: Please provide a valid task number!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks in your to-do list!")
        else:
            print("\n📋 Your To-Do List:")
            print("-" * 30)
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("-" * 30)
            print(f"Total tasks: {len(self.tasks)}")
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if self.tasks:
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
            if confirm == 'y' or confirm == 'yes':
                self.tasks.clear()
                self.save_tasks()
                print("✓ All tasks cleared!")
            else:
                print("Operation cancelled.")
        else:
            print("No tasks to clear!")

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("        TO-DO LIST MANAGER")
    print("="*40)
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Clear all tasks")
    print("5. Exit")
    print("="*40)

def main():
    """Main function to run the to-do list manager"""
    todo = TodoManager()
    
    print("Welcome to your Personal To-Do List Manager!")
    print(f"Tasks are saved in: {todo.filename}")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                todo.view_tasks()
            
            elif choice == '2':
                while True:
                    task = input("Enter new task: ")
                    todo.add_task(task)
                    
                    continue_adding = input("\nWould you like to add another task? (y/n): ").lower().strip()
                    if continue_adding not in ['y', 'yes']:
                        print("Returning to main menu...")
                        break
            
            elif choice == '3':
                todo.view_tasks()
                if todo.tasks:  # Only ask for removal if there are tasks
                    try:
                        task_num = int(input("Enter task number to remove: "))
                        todo.remove_task(task_num)
                    except ValueError:
                        print("Error: Please enter a valid number!")
            
            elif choice == '4':
                todo.clear_all_tasks()
            
            elif choice == '5':
                print("Thank you for using To-Do List Manager!")
                print("Your tasks have been saved. Goodbye! ")
                break
            
            else:
                print("Invalid choice! Please select 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! Your tasks have been saved. ")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()