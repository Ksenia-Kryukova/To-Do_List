import json
import csv
import argparse


GREETINGS = '''Добро пожаловать в To-Do List!
    Используйте комманды для работы со списками.
    Все доступные комманды можно увидеть по команде --help или -h'''
Q_NAME = 'Как будет называться новый список?'
Q_CONTINUE = 'Продолжить работу со списком? Введите да|нет'
LIST_READY = 'Список создан'
INPUT_NAME = 'Введите название списка, который хотите изменить'
ERROR_FileNotFound = '''У вас еще нет списка дел с таким названием.
    Попробуйте открыть другой или создать новый'''
REPEAT = 'Попробуйте еще раз.'
SELECT_ACTION = '''Какое действие вы хотите выполнить следующим?'''
NO_ACTION = 'Такого действия нет в списке. Попробуйте еще раз.'
SAVED = 'Изменения сохранены. До встречи!'
INPUT_TASK = 'Введите задачу: '
Q_CONTINUE_INPUT = 'Продолжить ввод задач? да|нет'
TASKS_READY = 'Задачи внесены в список'
Q_TASK_DEL = 'Введите номер задачи, которую хотите удалить'
TASK_DEL = 'Задача успешно удалена из списка'
SUCCESSFUL = 'Молодец! Ты выполнил все задачи)'
NO_NUMBER = 'Такого номера нет в списке, выберите другой'
Q_TASK_CHANGE = 'Введите номер задачи, которую хотите изменить: '
INPUT_TASK_CHANGED = 'Введите изменённую задачу: '


def load_todo_list(name: str):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            todo_list = json.load(file)
        return todo_list
    except FileNotFoundError:
        return ERROR_FileNotFound


def add_task(todo_list: list, task: str):
    while True:
        todo_list.append(task)
        print(Q_CONTINUE_INPUT)
        if input().lower() == 'нет':
            print(TASKS_READY)
            break


def del_task(todo_list: list, num: int):
    print(Q_TASK_DEL)
    try:
        del todo_list[num - 1]
        print(TASK_DEL)
        if len(todo_list) == 0:
            print(SUCCESSFUL)
    except IndexError:
        print(NO_NUMBER)


def change_task(todo_list: list, num: int, task: str):
    try:
        todo_list[num - 1] = task
    except IndexError:
        print(NO_NUMBER)


def get_list(todo_list: list):
    if len(todo_list) == 0:
        print(SUCCESSFUL)
    else:
        for num, task in enumerate(todo_list, 1):
            print(f'{num}. {task}')


def create_new_list(name: str, todo_list: list):
    with open(name, 'w', encoding='utf-8') as file:
        while True:
            task = input(INPUT_TASK)
            todo_list.append(task)
            print(Q_CONTINUE_INPUT)
            if input().lower() == 'нет':
                print(LIST_READY)
                break
        json.dump(todo_list, file)


def save_list(todo_list: list, name: str):
    with open(name, 'w', encoding='utf-8') as file:
        json.dump(todo_list, file)
    print(SAVED)


def change_list(name: str):
    todo_list = load_todo_list(name)
    while True:
        if args.add:
            add_task(todo_list, args.new_task)
        elif args.delete:
            del_task(todo_list, args.delete)
        elif args.change_task:
            change_task(todo_list, args.change_task, args.new_task)
        elif args.list:
            get_list(todo_list)
        elif args.save:
            save_list(todo_list, args.save)
            break
        else:
            print(NO_ACTION)


def start_program():
    if args.create:
        create_new_list(args.create, [])
    elif args.change_list:
        change_list(args.change_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа для управления списками дел')

    parser.add_argument('-al', '--all_lists',
                        help='Вывести все списки')
    parser.add_argument('-l', '--list',
                        help='Вывести все задачи списка')
    parser.add_argument('-c', '--create',
                        help='Создать новый список дел с указанным названием')
    parser.add_argument('-chl', '--change_list',
                        help='Изменить список дел по названию')
    parser.add_argument('-a', '--add',
                        help='Добавить новую задачу в список дел')
    parser.add_argument('-d', '--delete', type=int,
                        help='Удалить задачу по указанному номеру')
    parser.add_argument('-cht', '--change_task', type=int,
                        help='Изменить задачу по указанному номеру')
    parser.add_argument('-nt', '--new_task',
                        help='Текст измененной задачи')
    parser.add_argument('-s', '--save',
                        help='Сохранить список дел')

    args = parser.parse_args()

    print(GREETINGS)
    start_program()