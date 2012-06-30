'''
Created on 27 juin 2012

@author: Marc
'''

import CParser
import sys

class CGoogleSearchQueryFormatter:

    def __init__(self):
        self.parser = CParser.CParser()
        
    def test(self):
        self.simpleTest()
        self.simpleTestWithParanthese()
        self.simpleAnd()
        self.simpleOr()
        self.test1()
        self.test2()
        self.test3()
        
    def parse(self, toParse):
        self.parser.parse(toParse)
        
    def simpleTest(self):
        print("'isTrue = 1' =>")
        self.parser.parse("isTrue = 1")
        
    def simpleTestWithParanthese(self):
        print("'(isTrue = 1)' =>")
        self.parser.parse("(isTrue = 1)")
        
    def simpleAnd(self):
        print("'(isTrue = 1 AND bidule = string)' =>")
        self.parser.parse("(isTrue = 1 AND bidule = string)")
        
    def simpleOr(self):
        print("'(isTrue = 1 OR bidule = string)' =>")
        self.parser.parse("(isTrue = 1 OR bidule = string)")
        
    def test1(self):
        print("'((isTrue = 1 AND bidule = string) OR bidule = otherString)' =>")
        self.parser.parse("((isTrue = 1 AND bidule = string) OR bidule = otherString)")
        
    def test2(self):
        print("'((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString))' =>")
        self.parser.parse("((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString))")
        
    def test3(self):
        print("'((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString)) AND statement' =>")
        self.parser.parse("((isTrue = 1 AND bidule = string) OR (isTrue = false AND bidule = otherString)) AND statement")

formatter = CGoogleSearchQueryFormatter()

if (len(sys.argv) > 1):
    if(sys.argv[1] == "-h" or sys.argv[1] == "-?"):
        print("Hello World!")
        print("""Usage : python CGoogleSearchQueryFormatter.py [-h | -? | -test] [string arg]
                    -h / -? : Display this help
                    -test : Run the built in test""")
    elif(sys.argv[1] != "-test"):
        formatter.parse(sys.argv[1])
    else:
        formatter.test()
else:
    formatter.test()