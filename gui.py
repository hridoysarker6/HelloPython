from math import trunc

import func
import FreeSimpleGUI as sg

label =sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
button = sg.Button("Add")

list_box = sg.Listbox(values=func.get_todos(),key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

layouts = [
    [label],
    [input_box,button],
    [list_box,edit_button]
]
window = sg.Window("Todo Application", layout=layouts)

while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos = func.get_todos()
            new_todos = values['todo']+"\n"
            todos.append(new_todos)
            func.write_todos(todos)
            window['todos'].update(todos)

        case 'todos':
            window['todo'].update(values['todos'][0])

        case 'Edit':
            todos_to_edit = values['todos'][0]
            new_todos = values['todo']+"\n"

            todos = func.get_todos()
            index = todos.index(todos_to_edit)
            todos[index] = new_todos
            func.write_todos(todos)
            window['todos'].update(todos)

        case sg.WINDOW_CLOSED:
            break

window.close()