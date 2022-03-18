import os
import json


f = open('settings.json','r')
settings = json.loads(f.read())
f.close()


def backupFiles():
    filesArray = []
    path = settings["game_folder"] + "\\" + settings["mm_folder"] + "\\" + settings["bkp_files"]
    for root, dirs, files in os.walk(path):
        for file in files:
                filePath = os.path.join(root, file).replace(path+"\\","")
                filesArray.append(filePath)
    return filesArray

def modFiles():
    filesArray = []
    path = settings["game_folder"] + "\\" + settings["mm_folder"] + "\\" + settings["mm_files"]
    for root, dirs, files in os.walk(path):
        for file in files:
                filePath = os.path.join(root, file).replace(path+"\\","")
                filesArray.append(filePath)
    return filesArray
