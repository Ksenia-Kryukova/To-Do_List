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