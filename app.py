import time

from func import get_todos, write_todos

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_promt = 'type add, show, edit, complete or exit: '
    user_action = input(user_promt).strip()

    if user_action.startswith('add'):
        todo = user_action[4:] +'\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    if user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.title()
            print(f"{index+1}- {item.strip()}" )

    if user_action.startswith('exit'):
        break

    if user_action.startswith('edit'):
        number = int(user_action[5:])
        number = number -1
        todo = input('Enter a todo: ')+'\n'
        todos = get_todos()
        todos[number] = todo

        write_todos(todos)

    if user_action.startswith('complete'):
        number = int(user_action[9:])
        number = number - 1
        todos = get_todos()
        todos.pop(number)

        write_todos(todos)


print('done')

