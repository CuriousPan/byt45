
class PowerGenerator():
    def __init__(self, producer, voltage):
        self.producer = producer
        self.voltage = voltage

    def printPowerGenerator(self):
        print("Producer: " + self.producer)
        print("Voltage: " + str(self.voltage))
