
class DivisionHandler():

    def __init__(self):
        self.nextHandler = None

    def setNextHandler(self, handler):
        self.nextHandler = handler

    def handle(self, calculations):
        if (calculations.get_sign() == "/"):
            print(str(calculations.get_number1()) + " " + calculations.get_sign() + " " + str(calculations.get_number2()) + " = " + str(calculations.get_number1() / calculations.get_number2()))
            return
        if (self.nextHandler == None):
            print("+, -, * and / operations are supported only")
            return
        self.nextHandler.handle(calculations);

