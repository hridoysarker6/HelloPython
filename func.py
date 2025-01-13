def get_todos(file_name='todos.txt'):
    with open(file_name,'r') as file:
        todos = file.readlines()
    return  todos


def write_todos(todos,file_name='todos.txt'):
    with open(file_name, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print('hello')