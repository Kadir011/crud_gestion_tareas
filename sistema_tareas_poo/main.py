from tasks_crud import TaskCrud
import time 

def main():
    user = input('User: ')
    crud = TaskCrud()

    while True:
        print(f'\nWelcome {user}!')
        print('\n----- OPTION MENU -----')
        print('1. View Tasks\n2. Add Task\n3. Search Task\n4. Update Task\n5. Delete Task\n6. Mark Task as Complete\n7. Exit')

        try:
            opc = int(input('Option: '))

            match opc:
                case 1:
                    crud.show_task()
                case 2:
                    crud.add_task()
                case 3:
                    crud.search_task()
                case 4:
                    crud.update_task()
                case 5:
                    crud.delete_task()
                case 6:
                    crud.mark_task_as_done()  
                case 7:
                    print(f'\nGoodbye {user}!\n')
                    break
                case _:
                    print("\nInvalid option! Please, enter the correct option.\n")
                    time.sleep(5)
        except ValueError:
            print("\nInvalid option! Please, enter the correct option.\n")
            continue

if __name__ == "__main__":
    main()



