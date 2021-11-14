
class Body():
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color

    def printBody(self):
        print("Producer: " + self.producer)
        print("Color: " + self.color)
