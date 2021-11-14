
class Legs():
    def __init__(self, producer, color, height):
        self.producer = producer
        self.color = color
        self.height = height
        
    def printLegs(self):
        print("Producer: " + self.producer)
        print("Color: " + self.color)
        print("Height: " + str(self.height))
