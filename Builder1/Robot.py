from RobotBuilder import *

class Robot():
    def __init__(self, builder):
        self.head = builder.head
        self.body = builder.body
        self.legs = builder.legs
        self.arms = builder.arms
        self.gun = builder.gun
        self.powerGenerator = builder.powerGenerator
        self.armor = builder.armor

    def printRobot(self):
        print("Head: ")
        self.head.printHead()
        print()

        print("Body: ")
        self.body.printBody()
        print()

        print("Legs: ")
        self.legs.printLegs()
        print()

        print("Arms: ")
        self.arms.printArms()
        print()

        if (self.gun != None):
            print("Gun: ")
            self.gun.printGun()
            print()
        
        print("Power generator: ")
        self.powerGenerator.printPowerGenerator()
        print()

        if (self.armor != None):
            print("Armor: ")
            self.armor.printArmor()
            print()
