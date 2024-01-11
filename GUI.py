import PySimpleGUI as sg
import vernier_to_plt
from datetime import date
from os import chdir
"""
A simple script to run a GUI of my graph maker.
"""
print("loading window...")
layout  =[
    [sg.Titlebar("Vernier to CSV")],
    [sg.Text("Please input the location of the CSV file"),sg.InputText("../experiment.csv")],
    [sg.Text("Please input the number of columns in the file"),sg.InputText()],
    [sg.Text("Input name of output file"),sg.InputText((str(date.today())+"_test"))],
    [sg.Text("Input subject of graph E.g a bouncing ball"),sg.InputText()],
    [sg.Checkbox("Use absolute value?")],
    [sg.Text("Colour of line:")],
    [sg.Combo(['red','blue','magenta','cyan','yellow','black'],'blue')],
    [sg.Checkbox("Curve of best fit?")],
    [sg.Text("If using curve of best fit, please input the degrees of the polynomial E.g (x-a)^3 where 3 is inputed"),sg.InputText("3")],
    [sg.Text("Error of x and error of y."),sg.InputText("0"),sg.InputText("0")],
    [sg.Button("Submit")],
    [sg.Text("Processed, you can quite now.").hide_row()],
    [sg.Button("Close")]
]
window = sg.Window("Vernier to CSV",layout,disable_minimize=True,resizable=True)
print("window loaded.")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    elif event == "Submit":
        file_path = values[0].strip('"')
        csv = vernier_to_plt.CsvToPlt(file_path,int(values[1]),values[4])
        csv.compile_all_data(values[2],values[3],colour=values[5],lobf=not values[6],degree=int(values[7]),xerror=float(values[8]),yerror=float(values[9]))
        window["element"].unhide_row
    elif event == "debug":
        print("foobar")