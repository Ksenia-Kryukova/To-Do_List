import json
import argparse


GREETINGS = '''Добро пожаловать в To-Do List!
    Используйте комманды для работы со списками.
    Все доступные комманды можно увидеть по команде --help или -h'''
LIST_READY = 'Список создан'
ERROR_FileNotFound = '''У вас еще нет списка дел с таким названием.
    Попробуйте открыть другой или создать новый'''
SAVED = 'Изменения сохранены. До встречи!'
INPUT_TASK = 'Введите задачу: '
Q_CONTINUE_INPUT = 'Продолжить ввод задач? да|нет'
TASK_DEL = 'Задача успешно удалена из списка'
SUCCESSFUL = 'Молодец! Ты выполнил все задачи)'
NO_NUMBER = 'Такого номера нет в списке, выберите другой'


class My_list:
    class Task:
        def __init__(self, task):
            self.task = task

    def add_task(self, todo_list: list, task: str):
        todo_list.append(task)

    def del_task(self, todo_list: list, num: int):
        try:
            del todo_list[num - 1]
            print(TASK_DEL)
            if len(todo_list) == 0:
                print(SUCCESSFUL)
        except IndexError:
            print(NO_NUMBER)

    def change_task(self, todo_list: list, num: int, task: str):
        try:
            todo_list[num - 1] = task
        except IndexError:
            print(NO_NUMBER)

    def get_list(self, name: str):
        todo_list = load_todo_list(name)
        if len(todo_list) == 0:
            print(SUCCESSFUL)
        else:
            for num, task in enumerate(todo_list, 1):
                print(f'{num}. {task}')

    def create_new_list(self, name: str, todo_list: list):
        with open(name, 'w', encoding='utf-8') as file:
            while True:
                task = input(INPUT_TASK)
                todo_list.append(task)
                print(Q_CONTINUE_INPUT)
                if input().lower() == 'нет':
                    print(LIST_READY)
                    break
            json.dump(todo_list, file)

    def change_list(self, name: str):
        todo_list = load_todo_list(name)
        if args.add:
            add_task(todo_list, args.add)
        elif args.delete:
            del_task(todo_list, args.delete)
        elif args.change_task:
            change_task(todo_list, args.change_task, args.new_task)
        with open(name, 'w', encoding='utf-8') as file:
            json.dump(todo_list, file)
        print(SAVED)


class Saver:
    def save_list(self, todo_list: list, name: str):
        with open(name, 'w', encoding='utf-8') as file:
            json.dump(todo_list, file)
        print(SAVED)


class Loader:
    def load_todo_list(self, name: str):
        try:
            with open(name, 'r', encoding='utf-8') as file:
                todo_list = json.load(file)
            return todo_list
        except FileNotFoundError:
            return ERROR_FileNotFound


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=GREETINGS)

    parser.add_argument('-al', '--all_lists',
                        help='Вывести все списки')
    parser.add_argument('-l', '--list',
                        help='Вывести все задачи указанного списка')
    parser.add_argument('-c', '--create',
                        help='Создать новый список дел с указанным названием')
    parser.add_argument('-chl', '--change_list',
                        help='Изменить список дел с указанным названием')
    parser.add_argument('-a', '--add',
                        help='Добавить новую задачу в список дел')
    parser.add_argument('-d', '--delete', type=int,
                        help='Удалить задачу по указанному номеру')
    parser.add_argument('-cht', '--change_task', type=int,
                        help='Изменить задачу по указанному номеру на новую')
    parser.add_argument('-nt', '--new_task',
                        help='Текст измененной задачи')

    args = parser.parse_args()

