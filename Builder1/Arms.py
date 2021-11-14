
class Arms():
    def __init__(self, producer, color, length):
        self.producer = producer
        self.color = color
        self.length = length

    def printArms(self):
        print("Producer: " + self.producer)
        print("Color: " + self.color)
        print("Length: " + str(self.length))
