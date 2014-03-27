# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import codecs
import sys
import Tkinter
from pprint import pprint

class Expert :
    baseName = ""
    base = dict()
    knownData = dict()
    stack = []
    hasQuestions_ = false

    def __init__(self, fileName) :
        with open(fileName, "r") as data_file:    
            data = json.load(data_file, "utf-8")
        print(data)
        mapData = dict()
        print len(data["data"])
        for entry in data["data"] :
            key = entry["THEN"].keys()[0]
            if key not in mapData :
                mapData[key] = []
            mapData[key].append((entry["IF"], entry["THEN"][key]))
        print mapData["body type"]
        self.base = mapData
        self.baseName = data["base_name"]
        self.stack.append(data["aim"])
    
    def hasQuestions(self) :
        return hasQuestions_
    
    def getNextQuestion(self) :
        if stack :
            aim = stack[-1]
            if aim in knownData :
                del stack[-1]
                return
            else :
                
        else :
            hasQuestions_ = false
        return
    
exp = Expert("tmp.json")

exp.getNextQuestion()

# <codecell>

import easygui as eg
import sys

title = "Message from test1.py"
eg.msgbox("Hello, world!", title)
while 1:
    

    msg ="What is your favorite flavor?"
    title = "Ice Cream Survey"
    choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
    choice = eg.choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    #eg.msgbox("You chose: " + str(choice), "Survey Result")

    #msg = "Do you want to continue?"
    #title = "Please Confirm"
    if choice:     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel

# <codecell>

from Tkinter import *
import ttk

class App:

    value_of_combo = 'X'


    def __init__(self, parent):
        self.parent = parent
        self.combo()
        
    def newselection(self, event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
        self.box.bind("<<ComboboxSelected>>", self.newselection)
        self.box['values'] = ('X', 'Y', 'Z')
        self.box.current(0)
        self.box.grid(column=0, row=0)

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()

# <codecell>


