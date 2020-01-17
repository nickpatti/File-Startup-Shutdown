import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetype=(("executables", "*exe"), ("all files", "*.*")))

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="lightgrey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


def closeApps():
    x = 0
    for app in apps:
        appi = os.path.basename(apps[x])
        os.system(f'TASKKILL /F /IM {appi}')
        x += 1


canvas = tk.Canvas(root, height=700, width=700, bg="green4")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", bg="green4", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", bg="green3", command=runApps)
runApps.pack()

closeApps = tk.Button(root, text="Close Apps", bg="red", command=closeApps)
closeApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
