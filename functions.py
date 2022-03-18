import json
import shutil
from tkinter import *
import os
import files as fl

def launchGame():
    os.startfile("D:\\SteamLibrary\\steamapps\\common\\F1 2021\\F1_2021_dx12.exe")
    return True

def replaceFiles(toCopy,gameRoot,files):
    for file_ in files:
        copyPath = toCopy + "\\" + file_
        rootPath = gameRoot + "\\" + file_
        if os.path.exists(rootPath):
            os.remove(rootPath)
        print("Moving File...")
        shutil.copy(copyPath, rootPath)
        print("Moved: "+ copyPath)
    print("Finished!")
        

def installMods():
    f = open('settings.json','r')
    settings = json.loads(f.read())
    f.close()
    modsFiles = settings["game_folder"] + "\\" + settings["mm_folder"] + "\\" + settings["mm_files"]
    gameRoot = settings["game_folder"]
    replaceFiles(modsFiles,gameRoot,fl.modFiles())
    return True

def removeMods():
    f = open('settings.json','r')
    settings = json.loads(f.read())
    f.close()
    backupFiles = settings["game_folder"] + "\\" + settings["mm_folder"] + "\\" + settings["bkp_files"]
    gameRoot = settings["game_folder"]
    replaceFiles(backupFiles,gameRoot,fl.backupFiles())
    return True

def setGameFolder(location):
    location = location.get()
    with open('settings.json') as f:
        data = json.load(f)

    data['game_folder'] = location

    print(data['game_folder'])

    with open('settings.json', 'w') as f:
        json.dump(data, f)
    
    return True
