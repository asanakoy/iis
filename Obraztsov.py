# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import codecs
import sys
import Tkinter
import easygui as eg
from pprint import pprint

def getDictVal(dictionary, key) :
    if key not in dictionary :
        return None
    return dictionary[key]

class Expert :
    mainAim = ""
    baseName = ""
    rules = dict()
    answerVariants = dict()
    knownData = dict()
    aimStack = []
    rulesStack = []
    hasQuestions_ = False
    
    def addAnswerVariant(self, key, answerVariant) :
        if key not in self.answerVariants :
            self.answerVariants[key] = set()
        self.answerVariants[key].add(answerVariant)
    
    def __init__(self, fileName) :
        with open(fileName, "r") as data_file:    
            data = json.load(data_file, "utf-8")
        #print(data)
        mapData = dict()
        print len(data["data"])
        for entry in data["data"] :
            key = entry["THEN"].keys()[0]
            if key not in mapData :
                mapData[key] = []
            mapData[key].append((entry["IF"], entry["THEN"][key]))
            self.addAnswerVariant(key, entry["THEN"][key])
            for key_, answerVariant in entry["IF"].items() :
                self.addAnswerVariant(key_, answerVariant)
        #print mapData["body type"]
        self.rules = mapData
        self.baseName = data["base_name"]
        self.mainAim = data["aim"]
        self.aimStack.append(self.mainAim)
    
    def hasQuestions(self) :
        return self.hasQuestions_
        
    def getQuestion(self, aim) :
        msg ="Choose %s :" % aim
        if aim == self.mainAim :
            self.knownData[aim] = None
            print "[LOG] Don't know"
            return False
        choice = eg.choicebox(msg, self.baseName, list(self.answerVariants[aim]))
        #eg.msgbox("You chose: " + str(choice), "Survey Result")
        
        if choice:     # show a Continue/Cancel dialog
            self.setAnswer(aim, str(choice))
        else:
            sys.exit(0)           # user chose Cancel
        return True

    def getNextQuestion(self) :
        while self.aimStack :
            print "aimStack top:",  self.aimStack
            try:
                print "rulesStack top:", self.rulesStack[-1][1][0] 
            except (IndexError, TypeError): 
                print "rulesStack top: []"
            

                
            aim = self.aimStack[-1]
            if aim in self.knownData :
                del self.aimStack[-1]
                if self.rulesStack[-1][0] == aim :
                    del self.rulesStack[-1]
            else :
                if not  self.rulesStack or self.rulesStack[-1][0] != aim :
                    self.rulesStack.append((aim, getDictVal(self.rules, aim)))
                
                if not self.rulesStack[-1][1] :
                        return self.getQuestion(aim)
                flagContinue = False
                for key, val in self.rulesStack[-1][1][0][0].items() : 
                    if key in self.knownData and self.knownData[key] != val :
                        del self.rulesStack[-1][1][0]
                        print "FALSE For the top rule. Drop it"
                        flagContinue = True
                        break
                    if key not in self.knownData :
                        self.aimStack.append(key)
                        flagContinue = True
                        break
                if flagContinue : 
                    if not self.rulesStack[-1][1]:
                        return self.getQuestion(self.mainAim)
                    continue
                else :
                    self.setAnswer(aim, self.rulesStack[-1][1][0][1])
        return None
    
    def setAnswer(self, key, value) :
        self.knownData[key] = value
        print "[LOG] Know:", key, "=", self.knownData[key]
        
    def GetResult(self) :
        if not self.knownData[self.mainAim] :
            return "Unknown car"
        return "%s is %s" %(self.mainAim, self.knownData[self.mainAim])

def main() :
    exp = Expert("tmp.json")
    print "[LOG] expert initialized"
    while exp.getNextQuestion() :
        pass
    eg.msgbox(msg = exp.GetResult(), title = "Aknowledgement complete!")

    
if __name__ == "__main__":
    main()

# <codecell>


# <codecell>


