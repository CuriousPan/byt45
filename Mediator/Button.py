class Button():

    def __init__(self, text, code, mediator):
        self.text = text
        self.mediator = mediator
        self.code = code

    def click(self):
        self.mediator.handle(self.code)
