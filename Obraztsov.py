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
    rules = dict()
    knownData = dict()
    aimStack = []
    rulesStack = []
    hasQuestions_ = False

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
        self.rules = mapData
        self.baseName = data["base_name"]
        self.aimStack.append(data["aim"])
        print self.rulesStack
    
    def hasQuestions(self) :
        return self.hasQuestions_
    
    def getNextQuestion(self) :
        while self.aimStack :
            aim = self.aimStack[-1]
            if aim in self.knownData :
                del self.aimStack[-1]
                if self.rulesStack[-1][0] == aim :
                    del self.rulesStack[-1]
            else :
                rules = self.rules[aim]
                self.rulesStack.append((aim, rules))
                
                
                aim = 
        else :
            self.hasQuestions_ = false
        return
    
    def setAnswer(self, key, value) :
        self.knownData[key] = value
        
    def GetResult(self) :
        return 
    
exp = Expert("tmp.json")

exp.getNextQuestion()

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


