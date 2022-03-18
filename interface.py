import functions as fc
from tkinter import *
import json

# Json
f = open('settings.json','r')
settings = json.loads(f.read())
f.close()
# 
app = Tk()


# ======================
# gameFolder
gameFolder_value = StringVar()
gameFolder_label = Label(app, text='Game Folder', font=('bold', 14), pady=20)
gameFolder_label.grid(row=0, column=0, sticky=W)
gameFolder_entry = Entry(app, textvariable=gameFolder_value)
gameFolder_entry.grid(row=0, column=1)
# Buttons
setGf_btn = Button(app, text='Set gameFolder', width=12, command=lambda: fc.setGameFolder(gameFolder_value))
setGf_btn.grid(row=0, column=2, pady=20)

# ======================

# Buttons
install_btn = Button(app, text='Install Mods', width=12, command=fc.installMods)
install_btn.grid(row=1, column=0, pady=20)

# Buttons
remove_btn = Button(app, text='Remove Mods', width=12, command=fc.removeMods)
remove_btn.grid(row=1, column=1, pady=20)

# PlayGame
playGame_btn = Button(app, text='Launch F1', width=12, command=fc.launchGame)
playGame_btn.grid(row=2, column=0, pady=20)

# GameLocation
gameLocation_label = Label(app, text=settings["game_folder"], font=('arial', 12), pady=0)
gameLocation_label.grid(row=20, column=0, sticky=W)
# Mods On
labelText = "Mod Installed? " + settings["modsOn"]
gameLocation_label = Label(app, text=labelText, font=('arial', 12), pady=0)
gameLocation_label.grid(row=19, column=0, sticky=W)

app.title("F1 Switcher")
app.geometry("700x300")

# Start program

app.mainloop()