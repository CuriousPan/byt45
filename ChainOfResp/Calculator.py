from AdditionHandler import *
from SubstractionHandler import *
from MultiplicationHandler import *
from DivisionHandler import *
from Calculations import *

class Calculator():

    def __init__(self):
        self.chain1 = AdditionHandler()
        self.chain2 = SubstractionHandler()
        self.chain3 = MultiplicationHandler()
        self.chain4 = DivisionHandler()

        self.chain1.setNextHandler(self.chain2)
        self.chain2.setNextHandler(self.chain3)
        self.chain3.setNextHandler(self.chain4)

    def start(self):
        print("Use formats like:")
        print("1 + 1")
        print("1 - 1")
        print("1 * 1")
        print("1 / 1")
        while (True):
            inputStr = input(">:")
            splittedStr = inputStr.split(" ")
            if (len(splittedStr) != 3):
                print("Incorrect format 1")
                continue
            try:
                n1 = float(splittedStr[0])
                n2 = float(splittedStr[2])
            except:
                print("Incorrect format 2")
                continue

            sign = splittedStr[1]
            if (sign != "+" and sign != "-" and sign != "*" and sign != "/"):
                print("Incorrect format 3")
                continue
            if (sign == "/" and n2 == 0):
                print("Division by 0")
                continue

            result = self.chain1.handle(Calculations(n1, n2, sign))
