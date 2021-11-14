
class Head():
    def __init__(self, producer, visionSystemName):
        self.producer = producer
        self.visionSystem = visionSystemName

    def printHead(self):
        print("Producer: " + self.producer)
        print("Vision system: " + self.visionSystem)
