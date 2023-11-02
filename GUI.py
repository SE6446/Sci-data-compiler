import PySimpleGUI as sg
import vernier_to_plt
from time import sleep
layout  =[
    [sg.Titlebar("Vernier to CSV")],
    [sg.Text("Hello world")],
    [sg.Text("Please input the location of the CSV file"),sg.InputText()],
    [sg.Text("Input name of output file"),sg.InputText()],
    [sg.Button("Submit")],
    [sg.Text(key="element")],
    [sg.Button("Close",visible=False,key="button")]
]
window = sg.Window("Vernier to CSV",layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close": # if user closes window or clicks cancel
        break
    elif event == "Submit":
        csv = vernier_to_plt.CsvToPlt(values[0])
        csv.compile_all_data(values[1])
        window["element"].update("Processed breaking in 5 seconds")
        sleep(5)
        break
