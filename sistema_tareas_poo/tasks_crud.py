from class_tarea import Task 
import os, json, time

class TaskCrud:
    def __init__(self):
        self.task_list = self.load_task_from_json()

    def save_task_from_json(self):
        with open('info_task.json', 'w', encoding='utf-8', errors='replace') as file:
            data = {task.name: task.status for task in self.task_list}
            json.dump(data, 
                      file, 
                      ensure_ascii=False, 
                      indent=4)

    def load_task_from_json(self):
        if os.path.exists('info_task.json'):
            try:
                with open('info_task.json', 'r', encoding='utf-8', errors='replace') as file:
                    data = json.load(file)
                    return [Task(name, status) for name, status in data.items()]
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading the task file. Starting with an empty task list.")
                return []
        return []

    def show_task(self):
        if not self.task_list:
            print('\nNo tasks registered!\n')
        else:
            print('\n---- TASK LIST ----')
            for i, task in enumerate(self.task_list):
                print(f'{i + 1}. {task}')

    def add_task(self):
        try:
            num_tasks = int(input('Enter the number of tasks:  '))

            if num_tasks < 1:
                raise ValueError('The amount of tasks must be positive!')

            for i in range(num_tasks):
                task_name = input(f'Enter task {i + 1}: ')
                new_task = Task(task_name)  
                self.task_list.append(new_task)

            self.save_task_from_json()
            print(f'\n{num_tasks} task(s) registered!\n')
        except ValueError as e:
            print(f'Invalid input: {e}')

    def search_task(self):
        entrance = input('Enter the word or index: ')

        if entrance.isdigit():
            num_task = int(entrance)

            if 1 <= num_task <= len(self.task_list):
                print(f'Task found: {self.task_list[num_task - 1]}')
            else:
                print('Number out of range!')
        else:
            searched_task = entrance.lower()
            coincidences = [task for task in self.task_list if searched_task in task.name.lower()]

            if coincidences:
                print(f"Matches found: {', '.join(str(task) for task in coincidences)}")
            else:
                print(f'No match found for {entrance}.')

    def update_task(self):
        try:
            task_index = int(input('Task number to update: ')) - 1

            if 0 <= task_index < len(self.task_list):
                new_task_name = input('New Task Name: ')
                self.task_list[task_index].name = new_task_name
                self.save_task_from_json()
                print('\nTask updated!\n')
            else:
                print('\nInvalid index!\n')
        except ValueError:
            print("\nInvalid option! Please, enter the correct option.\n")
            time.sleep(5)

    def delete_task(self):
        try:
            task_index = int(input('Task number to delete: ')) - 1

            if 0 <= task_index < len(self.task_list):
                self.task_list.pop(task_index)
                self.save_task_from_json()
                print('\nTask deleted!\n')
            else:
                print('\nInvalid index!\n')
        except ValueError:
            print("\nInvalid option! Please, enter the correct option.\n")
            time.sleep(5)

    def mark_task_as_done(self):
        try:
            task_index = int(input('Enter the task number to mark as completed: ')) - 1

            if 0 <= task_index < len(self.task_list):
                self.task_list[task_index].mark_as_done()
                self.save_task_from_json()
                print(f'Task {task_index + 1} marked as complete!')
            else:
                print('\nInvalid index!\n')
        except ValueError:
            print("\nInvalid input! Please, enter the correct task number.\n")
            time.sleep(5)







