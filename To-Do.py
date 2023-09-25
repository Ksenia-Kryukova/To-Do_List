import json


def load_todo_list(name: str) -> list:
    with open(name, 'r', encoding='utf-8') as file:
        todo_list = json.load(file)
        return todo_list


def add_task(todo_list: list):
    while True:
        task = input('Введите новую задачу: ')
        todo_list.append(task)
        print('Продолжить ввод задач? да|нет')
        if input().lower() == 'нет':
            print('Задачи внесены в список')
            break


def del_task(todo_list: list):
    print('Введите номер задачи, которую хотите удалить')
    try:
        del todo_list[int(input()) - 1]
        print('Задача успешно удалена из списка')
        if len(todo_list) == 0:
            print('Молодец! Ты выполнил все задачи)')
    except IndexError:
        print('Такого номера нет в списке, выберите другой')


def change_task(todo_list: list):
    num = input('Введите номер задачи, которую хотите изменить: ')
    try:
        todo_list[int(num) - 1] = input('Введите изменённую задачу: ')
    except IndexError:
        print('Такого номера нет в списке, выберите другой')


def get_list(todo_list: list):
    if len(todo_list) == 0:
        print('Молодец! Ты выполнил все задачи)')
    else:
        for num, task in enumerate(todo_list, 1):
            print(f'{num}. {task}')


def create_new_list(name: str):
    with open(name, 'w', encoding='utf-8') as file:
        todo_list = []
        while True:
            task = input('Введите задачу: ')
            todo_list.append(task)
            print('Продолжить ввод задач? да|нет')
            if input().lower() == 'нет':
                print('Новый список дел успешно создан')
                break
        json.dump(todo_list, file)


def save_list(todo_list: list, name: str):
    with open(name, 'w', encoding='utf-8') as file:
        json.dump(todo_list, file)
    print('Изменения сохранены. До встречи!')


def change_list(name: str):
    todo_list = load_todo_list(name)
    while True:
        print('''Какое действие вы хотите выполнить следующим?
        Выберите номер действия:
        1. Добавить новую задачу
        2. Удалить задачу
        3. Изменить задачу
        4. Посмотреть список задач
        5. Закончить работу со списком и сохранить изменения''')
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
            print('Такого действия нет в списке. Попробуйте еще раз.')


print('''Добро пожаловать в To-Do List!
Введите "1", если хотите создать новый список дел.
Введите "2", если хотите изменить существующий.''')
target = input()
if target == '1':
    print('Как будет называться новый список?')
    name = input()
    create_new_list(name)
    print('Продолжить работу со списком? Введите да|нет')
    answer = input()
    if answer.lower() == 'да':
        change_list(name)
    else:
        print('Список создан')
elif target == '2':
    print('Введите название списка, который хотите изменить')
    try:
        change_list(input())
    except FileNotFoundError:
        print('''У вас еще нет списка дел с таким названием.
        Попробуйте открыть другой или создать новый''')
else:
    print('Попробуйте еще раз.')
