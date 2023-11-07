import PySimpleGUI as sg
import vernier_to_plt
from time import sleep
from datetime import date
"""
A simple script to run a GUI of my graph maker.
"""
print("loading window...")
layout  =[
    [sg.Titlebar("Vernier to CSV")],
    [sg.Text("Hello world")],
    [sg.Text("Please input the location of the CSV file"),sg.InputText("experiment.csv")],
    [sg.Text("Please input the number of columns in the file"),sg.InputText()],
    [sg.Text("Input name of output file"),sg.InputText((date.today(),"_test"))],
    [sg.Text("Input subject of graph E.g a bouncing ball"),sg.InputText()],
    [sg.Checkbox("Use absolute?")],
    [sg.Button("Submit")],
    [sg.Text(key="element")]
]
window = sg.Window("Vernier to CSV",layout)
print("window loaded.")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close": # if user closes window or clicks cancel
        break
    elif event == "Submit":
        file_path = values[0].strip('"')
        csv = vernier_to_plt.CsvToPlt(file_path,int(values[1]),values[4])
        csv.compile_all_data(values[2],values[3])
        window["element"].update("Processed breaking in 5 seconds")
        sleep(5)
        break
