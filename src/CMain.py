'''
Created on 27 juin 2012

@author: Marc
'''

import CParser

class CMain:

    def __init__(self):
        self.parser = CParser.CParser()
        self.simpleTest()
        self.simpleTestWithParanthese()
        self.simpleAnd()
        self.simpleOr()
        self.test1()
        self.test2()
        self.test3()
        
    def simpleTest(self):
        print("'isTrue = 1' =>")
        print(self.parser.parse("isTrue = 1"))
        
    def simpleTestWithParanthese(self):
        print("'(isTrue = 1)' =>")
        print(self.parser.parse("(isTrue = 1)"))
        
    def simpleAnd(self):
        print("'(isTrue = 1 AND bidule = string)' =>")
        print(self.parser.parse("(isTrue = 1 AND bidule = string)"))
        
    def simpleOr(self):
        print("'(isTrue = 1 OR bidule = string)' =>")
        print(self.parser.parse("(isTrue = 1 OR bidule = string)"))
        
    def test1(self):
        print("'((isTrue = 1 AND bidule = string) OR bidule = otherString)' =>")
        print(self.parser.parse("((isTrue = 1 AND bidule = string) OR bidule = otherString)"))
        
    def test2(self):
        print("'((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString))' =>")
        print(self.parser.parse("((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString))"))
        
    def test3(self):
        print("'((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString)) AND statement' =>")
        print(self.parser.parse("((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString)) AND statement"))
        

parser = CMain()