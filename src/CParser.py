'''
Created on 27 juin 2012

@author: Marc
'''

class CParser:
    
    def getIndentation(self, x):
        toDisplay = ""
        for i in range(x):
            toDisplay = toDisplay + "    "
        return toDisplay
    
    def printStatement(self, indentation, statement):
        print(statement)
    
    def parse(self, stringToParse):
        x = 0
        toDisplay = ""
        for c in stringToParse:
            if c == '(':
                if toDisplay != "" and toDisplay.isspace() == False:
                    self.printStatement(self.getIndentation(x), toDisplay)
                toDisplay = self.getIndentation(x)
                print(toDisplay + "(")
                x = x + 1
                toDisplay = self.getIndentation(x)
            elif c == ")":
                if toDisplay != "" and toDisplay.isspace() == False:
                    self.printStatement(self.getIndentation(x), toDisplay)
                x = x - 1
                toDisplay = self.getIndentation(x)
                print(toDisplay + ")")
                toDisplay = self.getIndentation(x)
            elif (toDisplay != "" and toDisplay.isspace() == False) or c != ' ':
                toDisplay = toDisplay + c
        if toDisplay != "" and toDisplay.isspace() == False:
            self.printStatement(self.getIndentation(x), toDisplay)