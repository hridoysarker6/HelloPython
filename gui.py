import func
import FreeSimpleGUI as sg

label =sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
button = sg.Button(button_text="Submit",button_color="red")


window = sg.Window("Todo Application", layout=[[label],[input_box,button]])
window.read()
window.close()