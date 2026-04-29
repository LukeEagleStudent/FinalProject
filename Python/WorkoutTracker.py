import json, os
import FreeSimpleGUI as sg

FILE = "exercises.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def rows(data):
    return [[
        name,
        str(info.get("weight", "")),
        str(info.get("reps", ""))
    ] for name, info in sorted(data.items())]

data   = load()                          
layout = [
    [sg.Table(values=rows(data), headings=["Exercise", "Weight", "Reps"],
              key="-TABLE-", num_rows=8)],
    [sg.Text("Exercise:"), sg.Input(key="-NAME-")  ],
    [sg.Text("Weight:"),   sg.Input(key="-WEIGHT-")],
    [sg.Text("Reps:"),     sg.Input(key="-REPS-")  ],
    [sg.Button("Save"),    sg.Button("Close")       ],
]
window = sg.Window("My Tracker", layout, finalize=True)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Close"):
        break

    if event == "Save":
        name   = values["-NAME-"].strip().lower()
        weight = values["-WEIGHT-"].strip()
        reps   = values["-REPS-"].strip()

        try:
            weight_val = float(weight)
            reps_val = int(reps)
        except ValueError:
            sg.popup("Please enter a valid number for Weight and an integer for Reps.")
            continue

        data[name] = {"weight": weight_val, "reps": reps_val}
        save(data)
        window["-TABLE-"].update(values=rows(data))

window.close()