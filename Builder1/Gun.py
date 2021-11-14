
class Gun():
    def __init__(self, producer, type_of_gun, caliber):
        self.producer = producer
        self.type_of_gun = type_of_gun
        self.caliber = caliber

    def printGun(self):
        print("Producer: " + self.producer)
        print("Type of gun: " + self.type_of_gun)
        print("Caliber: " + str(self.caliber))
