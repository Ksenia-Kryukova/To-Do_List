import json


GREETINGS = '''Добро пожаловать в To-Do List!
    Введите "1", если хотите создать новый список дел.
    Введите "2", если хотите изменить существующий.'''
Q_NAME = 'Как будет называться новый список?'
Q_CONTINUE = 'Продолжить работу со списком? Введите да|нет'
LIST_READY = 'Список создан'
INPUT_NAME = 'Введите название списка, который хотите изменить'
ERROR_FileNotFound = '''У вас еще нет списка дел с таким названием.
    Попробуйте открыть другой или создать новый'''
REPEAT = 'Попробуйте еще раз.'
SELECT_ACTION = '''Какое действие вы хотите выполнить следующим?
        Выберите номер действия:
        1. Добавить новую задачу
        2. Удалить задачу
        3. Изменить задачу
        4. Посмотреть список задач
        5. Закончить работу со списком и сохранить изменения'''
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


def add_task(todo_list: list):
    while True:
        task = input(INPUT_TASK)
        todo_list.append(task)
        print(Q_CONTINUE_INPUT)
        if input().lower() == 'нет':
            print(TASKS_READY)
            break


def del_task(todo_list: list):
    print(Q_TASK_DEL)
    try:
        del todo_list[int(input()) - 1]
        print(TASK_DEL)
        if len(todo_list) == 0:
            print(SUCCESSFUL)
    except IndexError:
        print(NO_NUMBER)


def change_task(todo_list: list):
    num = input(Q_TASK_CHANGE)
    try:
        todo_list[int(num) - 1] = input(INPUT_TASK_CHANGED)
    except IndexError:
        print(NO_NUMBER)


def get_list(todo_list: list):
    if len(todo_list) == 0:
        print(SUCCESSFUL)
    else:
        for num, task in enumerate(todo_list, 1):
            print(f'{num}. {task}')


def create_new_list(name: str):
    with open(name, 'w', encoding='utf-8') as file:
        todo_list = []
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
        print(SELECT_ACTION)
        action = input()
        if action == '1':
            add_task(todo_list)
        elif action == '2':
            del_task(todo_list)
        elif action == '3':
            change_task(todo_list)
        elif action == '4':
            get_list(todo_list)
        elif action == '5':
            save_list(todo_list, name)
            break
        else:
            print(NO_ACTION)


def start_program():
    print(GREETINGS)
    target = input()
    if target == '1':
        print(Q_NAME)
        name = input()
        create_new_list(name)
        print(Q_CONTINUE)
        answer = input()
        if answer.lower() == 'да':
            change_list(name)
        else:
            print(LIST_READY)
    elif target == '2':
        print(INPUT_NAME)
        change_list(input())
    else:
        print(REPEAT)


if __name__ == '__main__':
    start_program()
