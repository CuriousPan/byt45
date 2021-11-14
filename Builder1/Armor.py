
class Armor():
    def __init__(self, producer, weight):
        self.producer = producer
        self.weight = weight
        
    def printArmor(self):
        print("Producer: " + self.producer)
        print("Weight: " + str(self.weight))
